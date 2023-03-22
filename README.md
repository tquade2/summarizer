# crispy-dollop
Long Text GPT-3 Summarizer

This code is a Python script that takes an input text file, splits it into multiple smaller files, and summarizes each smaller file using OpenAI's GPT-3 language model. It then combines all of the summaries into a single file and summarizes that file into a final summary.

Variables
input_file: The path to the input text file that you want to summarize.
output_dir: The path to the directory where you want to store the output files and final summary.
words_per_file: The number of words you want to include in each output file.

Functions
split_text(input_file, output_dir, words_per_file): This function splits the input text file into smaller files based on the specified number of words per file. The smaller files are stored in the specified output directory.
summarize_text(text): This function summarizes the input text using GPT-3 and returns a summary.
improve_text(text): This function improves the coherence and readability of the input text using GPT-3 and returns a summary.
summarize_output_files(output_dir): This function summarizes all of the output files in the specified directory using summarize_text(). The summaries are stored in a dictionary with the file names as keys and the summaries as values.

Execution
Set the input_file, output_dir, and words_per_file variables to the desired values.
Make sure that you have an OpenAI API key, and replace the existing key with your own key in the script.
Run the script. It will split the input file into smaller files, summarize each file, combine the summaries into a single file, and then summarize the final file. The final summary will be stored in a file called final_summary.txt in the specified output_dir.

Note: This script requires an internet connection and an OpenAI API key to run. The API key should be kept private and not shared with others.
