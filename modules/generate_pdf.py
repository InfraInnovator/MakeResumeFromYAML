# generate_pdf.py

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.colors import black
from reportlab.platypus.flowables import KeepTogether, HRFlowable
from reportlab.platypus import Table, TableStyle, PageBreak
import json
import argparse


def section_spacer():
    return Spacer(1, 12)

def generate(data, output_file, shared_state=None):

    # Check if shared state has specific data
    if 'keywords' in shared_state:
        # Process with these keywords
        print("Keywords available for use:", shared_state['keywords'])

    # Example usage to store data to shared_state
    # shared_state['pdf_generated'] = True

    print("Generating PDF .pdf file...")

    # Define the page margins
    top_margin = 0.3*inch
    left_margin = 0.35*inch
    right_margin = 0.35*inch
    bottom_margin = 0.5*inch

    normal_text_font_size = 10
    normal_text_leading = 10
    normal_text_space_after = 10

    list_leading = 12
    list_space_after = 0

    header_name_font_size = 24
    header_name_leading = 28
    header_name_space_after = 0

    header_contact_font_size = 10
    header_contact_leading = 0
    header_contact_links_leading = 15

    section_heading_font_size = 12
    section_heading_leading = 12

    subheader_font_size = 12
    subheading_leading = 0
    subheading_space_after = 18

    font_bold = 'Times-Bold'
    font_italic = 'Times-Italic'
    font_regular = 'Times-Roman'
    align_left = 0
    align_center = 1
    align_right = 2

    doc = SimpleDocTemplate(
                    output_file,
                    pagesize=letter,
                    topMargin=top_margin,
                    leftMargin=left_margin,
                    rightMargin=right_margin,
                    top_margin=top_margin,
                    bottom_margin=bottom_margin)

    story = []

    # Header - person's name
    header_name_style = ParagraphStyle('Header1',
                            fontSize=header_name_font_size,
                            leading=header_name_leading,
                            spaceAfter=header_name_space_after,
                            alignment=align_center,
                            fontName=font_bold)

    # Subheader
    header_subheader_style = ParagraphStyle('header3',
                            fontSize=subheader_font_size,
                            leading=subheading_leading,
                            spaceAfter=subheading_space_after,
                            alignment=align_center,
                            fontName=font_bold)

    # Subheader - Pronounds
    header_subheader_pronouns_style = ParagraphStyle('header4',
                            fontSize=subheader_font_size,
                            leading=subheading_leading,
                            spaceAfter=subheading_space_after,
                            alignment=align_center,
                            fontName=font_regular)


    # Contact info
    header_contact_style = ParagraphStyle('body',
                                          fontSize=header_contact_font_size,
                                          spaceAfter=header_contact_leading,
                                          alignment=align_center,
                                          fontName=font_regular)

    # Contact info Links to LinkedIn, GitHub, and Website
    header_contact_links_style = ParagraphStyle('body',
                                                fontSize=header_contact_font_size,
                                                spaceAfter=header_contact_links_leading,
                                                alignment=align_center,
                                                fontName=font_regular)


    # Heading for the sections (e.g. Professional Experience, Education, etc.)
    section_header_style = ParagraphStyle('Header2',
                            fontSize=section_heading_font_size,
                            leading=section_heading_leading,
                            spaceAfter=0,
                            alignment=align_left,
                            fontName=font_bold)

    # Company and Position
    company_style_name = ParagraphStyle('Header5',
                            fontSize=normal_text_font_size,
                            leading=normal_text_leading,
                            spaceAfter=10,
                            alignment=align_left,
                            fontName=font_bold)

    company_style_role = ParagraphStyle('Header6',
                            fontSize=normal_text_font_size,
                            leading=normal_text_leading,
                            spaceAfter=normal_text_space_after,
                            alignment=align_left,
                            fontName=font_italic)

    # Company location and dates
    company_style_location = ParagraphStyle('Header5',
                            fontSize=normal_text_font_size,
                            leading=normal_text_leading,
                            spaceAfter=normal_text_space_after,
                            alignment=align_right,
                            fontName=font_bold)

    company_style_dates = ParagraphStyle('Header6',
                            fontSize=normal_text_font_size,
                            leading=normal_text_leading,
                            spaceAfter=normal_text_space_after,
                            alignment=align_right,
                            fontName=font_italic)

    # Short job description
    job_description_style = ParagraphStyle('body',
                            leftIndent=0.25*inch,
                            fontSize=normal_text_font_size,
                            leading=normal_text_leading,
                            spaceAfter=normal_text_space_after,
                            fontName=font_italic)

    # Technologies used
    job_description_style_technologies_used = ParagraphStyle('body',
                            leftIndent=0.25*inch,
                            fontSize=normal_text_font_size,
                            # leading=normal_text_leading,
                            spaceAfter=normal_text_space_after,
                            fontName=font_italic)

    # Bullet points
    bullet_style = ParagraphStyle('Bullet',
                            leftIndent=0.25*inch,
                            fontSize=normal_text_font_size,
                            leading=list_leading,  # Adjust this value for line spacing
                            spaceAfter=list_space_after,  # Adjust this value to reduce space between bullet points
                            fontName=font_regular,
                            bulletText=u'\u2022')

    # Skills
    skill_style = ParagraphStyle('body',
                            fontSize=normal_text_font_size,
                            leading=list_leading,
                            spaceAfter=list_space_after,
                            alignment=align_left,
                            fontName=font_regular)

    # Education
    education_style = ParagraphStyle('body',
                            fontSize=normal_text_font_size,
                            leading=list_leading,
                            spaceAfter=list_space_after,
                            alignment=align_left,
                            fontName=font_regular)

    # Certifications and awards
    certifications_style = ParagraphStyle('body',
                            fontSize=normal_text_font_size,
                            leading=list_leading,
                            spaceAfter=list_space_after,
                            alignment=align_left,
                            fontName=font_regular,
                            bulletText=u'\u2022')

    # Professional memberships
    membership_style = ParagraphStyle('body',
                            fontSize=normal_text_font_size,
                            leading=list_leading,
                            spaceAfter=list_space_after,
                            alignment=align_left,
                            fontName=font_regular,
                            bulletText=u'\u2022')

    summary_of_qualifications_style = ParagraphStyle('body',
                            fontSize=normal_text_font_size,
                            leading=list_leading,
                            spaceAfter=list_space_after,
                            alignment=align_left,
                            fontName=font_regular,
                            bulletText=u'\u2022')

    # Header content
    story.append(Paragraph(data['header']['name'], header_name_style))

    # Add a line return followed by the pronouns if they exist
    if data['header'].get('pronouns'):
        story.append(Paragraph(data['header']['pronouns'], header_subheader_pronouns_style))

    # Subheader
    if data['header'].get('subheader'):
        story.append(Paragraph(data['header']['subheader'], header_subheader_style))

    contact_info_fields = [
    data['header'].get('phone', ''),
    f"<a href='mailto:{data['header'].get('email', '')}'>{data['header'].get('email', '')}</a>",
    data['header'].get('location', '')
    ]

    # Filter out empty strings and join with ' | '
    contact_info = ' | '.join(filter(bool, contact_info_fields))

    # Contact links
    links = []
    if data['header'].get('linkedin'):
        links.append(f"<a href='{data['header']['linkedin']}'>{data['header']['linkedin']}</a>")
    if data['header'].get('github'):
        links.append(f"<a href='{data['header']['github']}'>{data['header']['github']}</a>")
    if data['header'].get('website'):
        links.append(f"<a href='{data['header']['website']}'>{data['header']['website']}</a>")

    contact_links = ' | '.join(links)

    story.append(Paragraph(contact_info, header_contact_style))
    if contact_links:
        story.append(Paragraph(contact_links, header_contact_links_style))


    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_header_style))
    story.append(HRFlowable(width="100%", thickness=2, color=black)) # Horizontal line

    for job in data['professional_experience']:
        if job.get('pdf_page_break_before'):
            story.append(PageBreak())
        # Create a table for the company, position, location, and dates
        company_position_data = [
            [Paragraph(job['company'], company_style_name), Paragraph(job['location'], company_style_location)],
            [Paragraph(job['position'], company_style_role), Paragraph(job['dates'], company_style_dates)]
        ]
        company_position_table = Table(company_position_data, colWidths=[doc.width*0.6, doc.width*0.4])
        company_position_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0)
        ]))
        story.append(company_position_table)

        # Add a spacer between the company/position table and the job description
        story.append(Spacer(1, 2))

        # Job Description
        if job['description']:

            # Replace & with &amp; to avoid error
            job['description'] = job['description'].replace('&', '&amp;')

            # Check if the job description is empty
            story.append(Paragraph(job['description'], job_description_style))


        # Bullet Points
        bullet_points = []

        # Bullet Points
        for duty in job['duties']:
            #replace & with &amp; to avoid error
            duty = duty.replace('&', '&amp;')
            bullet_points.append(Paragraph(duty, bullet_style))

        story.append(KeepTogether(bullet_points))
        story.append(section_spacer())


        # Check if the technologies used key exists and has a value at index 0 (not empty)
        if job.get('technologies_used') and job['technologies_used']:


            # Get the list items for the technologies used key
            technologies_used = job['technologies_used']

            if technologies_used:
                # Create a string of technologies used that is comma-separated and starts with Technologies Used:
                tech_used = ', '.join(technologies_used)
                story.append(Paragraph(f"<u>Technology Stack</u>: {tech_used}", job_description_style_technologies_used))

            else:
                # Don't write anything, including a new line
                pass

    # Define a dictionary of handlers for each section
    section_handlers = {
        'skills': lambda section_data: (
            [PageBreak()] if section_data.get('pdf_page_break_before') else []
        ) + [
            Paragraph("SKILLS & INTERESTS", section_header_style),
            HRFlowable(width="100%", thickness=2, color=black),
        ] + (
            [Paragraph("<b>Skills:</b> " + ', '.join(section_data['skills']), skill_style)]
            if 'skills' in section_data and section_data['skills'] else []
        ) + (
            [Spacer(1, 12),  # This adds a 12-point space between the sections
            Paragraph("<b>Interests:</b> " + ', '.join(section_data['interests']), skill_style)]
            if 'interests' in section_data and section_data['interests'] else []
        ),

        'education': lambda section_data: (
            [PageBreak()] if section_data.get('pdf_page_break_before') else []
        ) + [
            Paragraph("EDUCATION", section_header_style),
            HRFlowable(width="100%", thickness=2, color=black),
            *[Paragraph(school, education_style) for school in section_data['education_entries']]
        ],
        'certifications': lambda section_data: (
            [PageBreak()] if section_data.get('pdf_page_break_before') else []
        ) + [
            Paragraph("CERTIFICATIONS AND AWARDS", section_header_style),
            HRFlowable(width="100%", thickness=2, color=black),
            *[Paragraph(cert, certifications_style) for cert in section_data['certs']]
        ],
        'memberships': lambda section_data: (
            [PageBreak()] if section_data.get('pdf_page_break_before') else []
        ) + [
            Paragraph("PROFESSIONAL MEMBERSHIPS", section_header_style),
            HRFlowable(width="100%", thickness=2, color=black),
            *[Paragraph(membership, membership_style) for membership in section_data['memberships']]
        ],
        'summary_of_qualifications': lambda section_data: (
            [PageBreak()] if section_data.get('pdf_page_break_before') else []
        ) + [
            Paragraph("SUMMARY OF QUALIFICATIONS", section_header_style),
            HRFlowable(width="100%", thickness=2, color=black),
            *[Paragraph(qualification, summary_of_qualifications_style) for qualification in section_data['qualifications']]
        ]
    }

    # Iterate over the keys in the data and generate the corresponding sections
    for key in data:
        if key in section_handlers:
            section_content = section_handlers[key](data[key])
            story.extend(section_content)

            # Only add a spacer if the next section exists
            if key != list(data.keys())[-1]:
                story.append(section_spacer())

    # Remove any trailing empty elements (optional but recommended)
    while story and isinstance(story[-1], (Spacer, HRFlowable)):
        story.pop()

    # Build the PDF
    doc.build(story)


def main():

    parser = argparse.ArgumentParser(description='Generate a PDF from JSON data.')
    parser.add_argument('data_file', help='Path to the JSON data file')
    parser.add_argument('output_file', help='Path to the output PDF file')

    args = parser.parse_args()

    with open(args.data_file, 'r') as file:
        data = json.load(file)

    generate_pdf(data, args.output_file)

if __name__ == "__main__":
    main()
