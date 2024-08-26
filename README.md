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
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python -m resumeConvertFromYAML.process_data -i ./_ResumeInput/sample_resume.yaml -o ./_ResumeOutput/sample_resume.pdf
```

# Building a module
```shell
python setup.py sdist bdist_wheel
```
