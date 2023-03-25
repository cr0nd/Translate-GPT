# File Translator using GPT-3-Turbo

This is a command line tool that uses OpenAI's GPT-3 language model to translate text from one language to another. The tool is designed to handle large files and can translate multiple files at once.

## Getting Started

To use this tool, you must have an OpenAI API key. If you don't have one already, you can sign up for an account on the OpenAI website.

Once you have your API key, you can set it as an environment variable by running the following command in your terminal:

```arduino
export OPENAI_API_KEY=your_api_key
```

Alternatively, you can add the following line of code at the beginning of the script:

```python
openai.api_key = "your_api_key"
```

You will also need to install the necessary dependencies by running the following command:

```bash
pip install openai tqdm
```

## Usage

To translate a single file, run the following command:

```bash
python translate.py /path/to/file.txt
```

To translate all text files in a directory (and its subdirectories), run the following command:

```bash
python translate.py /path/to/directory
```

Translated files will be saved in the same directory as the original files, with "-translated" added to the filename.

## Notes

- The tool is currently set up to translate English text to Chinese, but you can modify the source and target languages by changing the `source_language` and `target_language` variables at the beginning of the script.
- The `translate_text` function is set up to split text into sections of `2000` characters or less. You can adjust this limit by changing the `token_limit` argument in the `split_text` function.

## Acknowledgments

This tool was made possible by the OpenAI API and the `tqdm` package.