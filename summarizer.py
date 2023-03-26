# Summarizer
# By Taylor Quade

import os
import openai

# Variables
INPUT_FILE = r'your input file path here'
OUTPUT_DIR = r'YOUR OUTPUT DIRECTORY PATH'
openai.api_key = "YOUR API KEY HERE"
WORDS_PER_FILE = 400



def split_text(input_file, output_dir, words_per_file=400):
    # Check if output directory exists, and create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read in text from input file
    with open(input_file, 'r') as f:
        text = f.read()

    # Split text into individual words
    words = text.split()

    # Calculate number of files needed to hold all words
    num_files = len(words) // words_per_file + 1
    print(f"Splitting text into {num_files} files.")

    # Write words to output files
    for i in range(num_files):
        start_index = i * words_per_file
        end_index = start_index + words_per_file
        file_name = os.path.join(output_dir, f"output_{i+1}.txt")
        with open(file_name, 'w') as f:
            f.write(' '.join(words[start_index:end_index]))
        print(f"Created output file {file_name}.")

# Split the input file into multiple output files
split_text(input_file, output_dir, words_per_file)

# Define function to summarize text using GPT-3
def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        max_tokens = 150,
        prompt = f"Summarize the main points of this text in 140 tokens or less:\n\n{text}",
        temperature=0.5,
        n=1,
        stop=None,
        timeout=15)
    summary = response.choices[0].text.strip()
    return summary

# Define function to imrpove text using GPT-3
def improve_text(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = f"Combine this text into one cohesive summary in 400 tokens:\n\n{text}",
        temperature=0.5,
        max_tokens=410,
        n=1,
        stop=None,
        timeout=15)
    summary = response.choices[0].text.strip()
    return summary

def summarize_output_files(output_dir):
    summaries = {}
    desired_order = [f"output_{i}.txt" for i in range(1, len(os.listdir(output_dir))+1)]
    for filename in desired_order:
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'r') as f:
            text = f.read()
        summary = summarize_text(text)
        summaries[filename] = summary
        print(f"Summarized {filename}")
    return summaries

# Summarize the text in each output file and store in a dictionary
summaries = summarize_output_files(output_dir)

# Write the summaries to a new file
output_file = os.path.join(output_dir, "all_summaries.txt")
with open(output_file, "w") as f:
    for filename, summary in summaries.items():
        f.write(f"{summary}\n\n")
print(f"Summaries written to {output_file}")

# Read in the all_summaries file
with open('C:\\Users\\tayqu\\Desktop\\output docs\\all_summaries.txt', 'r') as f:
    all_summaries = f.read()

# Summarize the entire text and write the result to a new file
with open('C:\\Users\\tayqu\\Desktop\\output docs\\final_summary.txt', 'w') as f:
    final_summary = improve_text(all_summaries)
    f.write(final_summary)
print("Final summary written to 'final_summary.txt'")
