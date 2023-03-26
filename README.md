# Summarizer

This repository contains code for summarizing text using OpenAI's GPT-3. The code splits input text into multiple output files, summarizes each file using GPT-3, and writes the summaries to a new file.

## Variables

The following variables are used in the code:

- `input_file`: The path to the input text file.
- `output_dir`: The path to the output directory where the summaries will be written.
- `words_per_file`: The number of words to include in each output file.
- `openai.api_key`: Your OpenAI API key.

## Usage

1. Set the `input_file`, `output_dir`, and `words_per_file` variables to your desired values.
2. Set your OpenAI API key as the `openai.api_key` variable.
3. Run the code.

The code will split the input text into multiple output files, summarize each file using GPT-3, and write the summaries to a new file called `final_summary.txt` in the output directory.

## Dependencies

The code requires the following packages:

- `os`
- `openai`

You can install these packages using pip:

