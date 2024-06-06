# generate_WordCloud.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate(data, output_file, shared_state=None):

    # Check if shared state has specific data
    if 'keywords' in shared_state:
        # Process with these keywords
        print("Keywords available for use:", shared_state['keywords'])

    # Example usage to store data to shared_state
    # shared_state['wordcloud_generated'] = True

    print("Generating wordcloud .png file...")

    # Collect all text from the resume
    resume_text = ""
    for section, content in data.items():
        if isinstance(content, dict):
            for key, value in content.items():
                resume_text += f"{value} "
        else:
            resume_text += f"{content} "

    # Configure and generate the word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords={"and", "to", "the", "of", "a", "in", "with", "for", "on", "at", "by", "as", "from", "is", "that", "an", "be", "this", "it", "or", "which", "all", "are", "also"}
    ).generate(resume_text)

    # Save the word cloud to the specified output file
    wordcloud.to_file(output_file)
    print(f"Word cloud saved to {output_file}")

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Generate a word cloud from JSON data.')
    parser.add_argument('data_file', help='Path to the JSON data file')
    parser.add_argument('output_file', help='Path to the output file where the word cloud will be saved')

    args = parser.parse_args()

    # Load the data from the specified JSON file
    with open(args.data_file, 'r') as file:
        data = json.load(file)

    # Call the generate function
    generate(data, args.output_file)
