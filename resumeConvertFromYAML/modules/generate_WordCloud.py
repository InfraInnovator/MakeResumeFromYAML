from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(data, output_file):

    print("Generating word cloud...")

    # Debugging: Print data in a pretty format
    # resume_text = ""
    # for section, content in data.items():
    #     resume_text += f"{section}:\n"
    #     if isinstance(content, dict):
    #         for key, value in content.items():
    #             resume_text += f"{key}: {value}\n"
    #     else:
    #         resume_text += f"{content}\n"
    #     resume_text += "\n"

    # Get all text from the resume
    resume_text = ""
    for section, content in data.items():
        if isinstance(content, dict):
            for key, value in content.items():
                resume_text += f"{value} "
        else:
            resume_text += f"{content} "

    # Generate word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords={"and", "to", "the", "of", "a", "in", "with", "for", "on", "at", "by", "as", "from", "is", "that", "an", "be", "this", "it", "or", "which", "all", "are", "also"}
        ).generate(resume_text)

    # Save the word cloud to a file
    wordcloud.to_file(output_file)
