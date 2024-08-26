# MakeResumeFromYAML

## Summary

This Python application generates a professional PDF document using
ReportLab. It structures the content based on the provided data,
including sections for professional experience, skills, education,
certifications, memberships, and qualifications.

## Benefits

Using this application allows for easy creation of well-formatted
and professional-looking resumes and other documents. It automates
the layout and styling, ensuring consistency and saving time
compared to manual formatting.

## Setup

### MacOS

- Developer tool is required
- Python 3.10+ has been tested
- Brew is required

You will likely need to install the following:

```bash
brew install pygobject3
brew install cairo pango gdk-pixbuf libffi
brew link pygobject3
```

### Script setup

```bash
git clone https://github.com/InfraInnovator/MakeResumeFromYAML.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
source venv/bin/activate
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume.pdf -m generate_pdf
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume_v2.pdf -m generate_pdf_v2
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume_v3.pdf -m generate_pdf_v3
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume.pdf -m generate_preview
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume.docx -m generate_docx
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume.png -m generate_wordcloud
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume.html -m generate_html
```

## Building a module

```shell
python setup.py sdist bdist_wheel
```
