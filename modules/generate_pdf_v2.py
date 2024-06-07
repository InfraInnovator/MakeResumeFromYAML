import argparse
import yaml
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
import os

def generate(data, output_file, template_file):
    print(f"Generating PDF using template: {template_file}")
    
    # Ensure template_file is a string
    if not isinstance(template_file, str):
        raise ValueError(f"Expected template_file to be a string, got {type(template_file)} instead")

    # Load Jinja2 template
    template_dir, template_name = os.path.split(template_file)
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    # Render template with data
    html_content = template.render(data)

    # Create PDF
    with open(output_file, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(html_content, dest=result_file)

    if pisa_status.err:
        print("Error creating PDF")
    else:
        print(f"PDF generated successfully: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate a PDF from YAML data using a template.')
    parser.add_argument('data_file', help='Path to the YAML data file')
    parser.add_argument('output_file', help='Path to the output PDF file')

    args = parser.parse_args()

    with open(args.data_file, 'r') as file:
        data = yaml.safe_load(file)

    generate(data, args.output_file, args.template)

if __name__ == "__main__":
    main()
