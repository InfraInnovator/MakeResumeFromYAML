import argparse
import yaml
from jinja2 import Environment, FileSystemLoader
import os
from weasyprint import HTML

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

    # Create PDF using WeasyPrint
    HTML(string=html_content).write_pdf(output_file)

    print(f"PDF generated successfully: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate a PDF from YAML data using a template.')
    parser.add_argument('data_file', help='Path to the YAML data file')
    parser.add_argument('output_file', help='Path to the output PDF file')
    parser.add_argument('--template', default='modules/generate_pdf_v2_templates/default_template.html', help='Path to the Jinja2 HTML template file')

    args = parser.parse_args()

    with open(args.data_file, 'r') as file:
        data = yaml.safe_load(file)

    generate(data, args.output_file, args.template)

if __name__ == "__main__":
    main()