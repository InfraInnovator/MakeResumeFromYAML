import argparse
import io
from io import BytesIO
from .modules.read_yaml import read_yaml
from .modules.generate_pdf import generate_pdf
from .modules.generate_docx import generate_docx
import yaml


def output_data(data, output):
    # Check if output is a string (file path) or file-like object
    if isinstance(output, str):
        if output.endswith(".pdf"):
            generate_pdf(data, output)
        elif output.endswith(".docx"):
            generate_docx(data, output)
        else:
            raise ValueError("Output file must be a .pdf or .docx file.")
    elif hasattr(output, 'write'):
        # If it's a file-like object, we assume PDF output
        # (modify as needed if you want to support DOCX output in this manner too)
        generate_pdf(data, output)
        return data, output
    else:
        raise ValueError("Invalid output. Expected a file path or a file-like object.")


def load_data(input_file):
    # Check if the input is a string (assumed to be a file path)
    if isinstance(input_file, str):
        if input_file.split(".")[-1] != "yaml":
            print("Invalid input file. Please provide a YAML file.")
            return

        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
    else:
        # Assume it's a file-like object
        if not hasattr(input_file, 'read'):
            print("Invalid input. Expected a file path or file-like object.")
            return

        data = yaml.safe_load(input_file)

    return data

def process_data(input_file, output_file_path, output_format='pdf'):
    print(f"Generating resume in {output_format} format...")

    if input_file is None:
        print("Please provide an input file")
        return

    try:
        data = load_data(input_file)
        if data is None:
            print("No data loaded from file")
            return

        if output_format == 'pdf':
            output_data(data, output_file_path)
        elif output_format == 'docx':
            output_data(data, output_file_path)
        else:
            raise ValueError("Unsupported output format")

        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate a resume from a YAML file.")
    parser.add_argument("-i", "--input_file", help="Path to the YAML file containing resume data.")
    parser.add_argument("-o", "--output_file", help="Path to the output file. Default is output.pdf.", default="resumes_output/output.pdf")

    args = parser.parse_args()

    # Determine the output format from the output file extension
    output_format = 'pdf' if args.output_file.endswith('.pdf') else 'docx'

    process_data(args.input_file, args.output_file, output_format)

if __name__ == '__main__':
    main()
