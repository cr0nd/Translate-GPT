import os
import sys
import openai
from tqdm import tqdm

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY", "your_api_key")

# Set source and target languages
source_language = "English"
target_language = "Chinese"
token_limit = 2000

# Function to translate text using GPT-3.5-turbo
def translate_text(text, source_language, target_language):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that translates {source_language} to {target_language}."},
            {"role": "user", "content": f"Translate the following {source_language} text to {target_language}: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

def split_text(text, token_limit):
    sections = []
    current_section = ""
    for line in text.splitlines():
        if len(current_section) + len(line) < token_limit:
            current_section += line + "\n"
        else:
            sections.append(current_section)
            current_section = line + "\n"
    sections.append(current_section)
    return sections

def translate_file(input_file, source_language, target_language):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    sections = split_text(content, token_limit)

    translated_sections = []
    for section in tqdm(sections, desc=f"Translating {input_file}"):
        translated = translate_text(section, source_language, target_language)
        translated_sections.append(translated)

    translated_content = "".join(translated_sections)

    output_file = os.path.splitext(input_file)[0] + "-translated" + os.path.splitext(input_file)[1]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_content)

    print(f"{input_file} has been translated to {target_language} and saved as {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename or directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isfile(input_path):
        translate_file(input_path, source_language, target_language)
    elif os.path.isdir(input_path):
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    translate_file(file_path, source_language, target_language)
    else:
        print("Invalid input path")
        sys.exit(1)

if __name__ == "__main__":
    main()
