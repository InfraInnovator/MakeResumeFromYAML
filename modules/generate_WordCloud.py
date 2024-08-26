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

    # Remove any non-alphanumeric characters
    resume_text = ''.join(e for e in resume_text if e.isalnum() or e.isspace())

    # Remove any extra spaces
    resume_text = ' '.join(resume_text.split())

    # Normalize the text to lowercase
    # Todo: Make this a CLI argument
    # resume_text = resume_text.lower()

    # Normaize similar words
    resume_text = resume_text.replace("aws", "AWS")


    # Configure and generate the word cloud
    wordcloud = WordCloud(
        width=1000,
        height=600,
        background_color='white',
        max_words=100,
        stopwords={
                "and", "to", "the", "of", "a", "in", "with", "for", "on",
                "at", "by", "as", "from", "is", "that", "an", "be",
                "this", "it", "or", "which", "all", "are", "also", "inc",
                "have", "has", "been", "using", "U.S.", "ensuring",
                "emphasizing", "other", "test", "SGsVPCVPCe", "acheiving",
                "location", "closely", "Inc.", "during", "Guided", "duties",
                "technologies_used", "responsibilities", "responsibility",
                "description", "company", "company_name", "company_location",
                "dates", "title", "title_name", "title_location", "title_dates",
             },
        # Todo: Make this a CLI argument
        colormap='viridis', # Green to yellow to blue
        # colormap='magma', # Black to red to yellow
        # colormap='plasma', # Blue to yellow to white
        # colormap='inferno', # Black to red to yellow to white
        # colormap='cividis', # Blue to yellow
        # colormap='spring', # Magenta to yellow
        # colormap='cool', # Cyan to magenta
        # colormap='twilight', # Blue to purple to pink
        # colormap='twilight_shifted', # Green to purple to pink
        # colormap='turbo', # Blue to green to yellow to red
        contour_width=1,     # Adding a slight contour to the words for better visibility
        contour_color='steelblue'
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
