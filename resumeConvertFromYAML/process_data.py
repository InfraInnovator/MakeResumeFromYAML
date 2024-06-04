import argparse
import io
from io import BytesIO
from .modules.read_yaml import read_yaml
from .modules.generate_pdf import generate_pdf
from .modules.generate_docx import generate_docx
import yaml
from .modules.generate_WordCloud import generate_wordcloud

def output_data(data, output, output_format_type):
    if isinstance(output, str):
        if output_format_type == "pdf":
            generate_pdf(data, output, style="default")
        elif output_format_type == "docx":
            generate_docx(data, output)
        elif output_format_type == "wordcloud":
            generate_wordcloud(data, output)
        else:
            raise ValueError("Output file must be a .pdf, .docx, or .png file.")
    elif hasattr(output, 'write'):
        if output_format_type == "pdf":
            generate_pdf(data, output, style="default")
        else:
            raise ValueError("Unsupported output format for file-like object.")
        return data, output
    else:
        raise ValueError("Invalid output. Expected a file path or a file-like object.")

def load_data(input_file):
    if isinstance(input_file, str):
        if not input_file.endswith(".yaml"):
            print("Invalid input file. Please provide a YAML file.")
            return
        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
    else:
        if not hasattr(input_file, 'read'):
            print("Invalid input. Expected a file path or file-like object.")
            return
        data = yaml.safe_load(input_file)
    return data

def process_data(input_file, output_file_path, output_format_type='pdf'):
    print(f"Generating resume in {output_format_type} format...")
    if input_file is None:
        print("Please provide an input file")
        return
    try:
        data = load_data(input_file)
        if data is None:
            print("No data loaded from file")
            return
        output_data(data, output_file_path, output_format_type)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the input file and try again.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate a resume from a YAML file.")
    parser.add_argument("-i", "--input_file", help="Path to the YAML file containing resume data.")
    parser.add_argument("-o", "--output_file", help="Path to the output file. Default is output.pdf.", default="resumes_output/output.pdf")
    parser.add_argument("-t", "--output_format_type", help="Output format. Options: pdf, docx, wordcloud. Default is pdf.", default="pdf")
    parser.add_argument("-s", "--style", help="Style for PDF output. Options: default, modern. Default is default.", default="default")

    args = parser.parse_args()

    # Check if the user specified an output format, if not read format from output file extension
    output_format_type = args.output_format_type
    if output_format_type is None:
        if args.output_file.endswith('.docx'):
            output_format_type = 'docx'
        elif args.output_file.endswith('.workdcloud'):
            # Rename the output file to .png
            args.output_file = args.output_file.replace('.wordcloud', '.png')
            output_format_type = 'wordcloud'
        else:
            output_format_type = 'pdf'

    process_data(args.input_file, args.output_file, output_format_type)

if __name__ == '__main__':
    main()
