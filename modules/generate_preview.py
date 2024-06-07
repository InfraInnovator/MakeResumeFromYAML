import argparse
import json

def generate(data, output_file, shared_state):
    # Since it's a preview, we assume no output file is needed and print to the console
    print("Preview of the Resume:")
    print(data)  # You might format this to display more nicely or handle the data as needed

def print_horizontal_line():
    """Prints a horizontal line for visual separation in the console."""
    print('-' * 80)

def print_header(data):
    """Prints the resume header information."""
    print(f"{data['header']['name'].upper()}")
    if 'subheader' in data['header']:
        print(f"{data['header']['subheader']}")
    print(f"Phone: {data['header']['phone']}, Email: {data['header']['email']}, LinkedIn: {data['header']['linkedin']}")

def print_professional_experience(data):
    """Prints the professional experience section."""
    print("\nPROFESSIONAL EXPERIENCE")
    print_horizontal_line()
    for job in data['professional_experience']:
        print(f"{job['company']} - {job['location']} ({job['dates']})")
        print(f"{job['position']}")
        print(f"{job['description']}")
        for duty in job['duties']:
            print(f"- {duty}")

def print_skills_and_interests(data):
    """Prints the skills and interests section."""
    if 'skills' in data:
        print("\nSKILLS")
        print(", ".join(data['skills']))
    if 'interests' in data:
        print("\nINTERESTS")
        print(", ".join(data['interests']))

def print_education(data):
    """Prints the education section."""
    if 'education' in data:
        print("\nEDUCATION")
        for item in data['education']:
            print(f"{item['degree']} - {item['institution']} ({item['year']})")

def preview_resume(data_file):
    """Load data from a JSON file and print a resume preview to the console."""
    with open(data_file, 'r') as file:
        data = json.load(file)

    print_header(data)
    print_professional_experience(data)
    print_skills_and_interests(data)
    print_education(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preview a resume from JSON data.')
    parser.add_argument('data_file', help='Path to the JSON data file')
    args = parser.parse_args()
    preview_resume(args.data_file)
