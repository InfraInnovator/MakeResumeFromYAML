# test_modules.py
import sys

import pytest
from resumeConvertFromYAML.process_data import main, load_modules  # import path

def test_module_loading():
    """Test if modules load correctly."""
    modules = load_modules()  # Ensure this function can be imported
    assert 'generate_docx' in modules  # Testing generate_docx

def test_output_file_generation(tmp_path):
    """Test if the output file is generated."""
    output_file = tmp_path / "output.docx"
    sys.argv = ['program_name', '-i', './_ResumeInput/sample_resume.yaml', '-o', str(output_file), '-m', 'generate_docx']
    main()  # main() will read from sys.argv

def test_output_file_generation_pdf(tmp_path):
    """Test if the output file is generated."""
    output_file = tmp_path / "output.pdf"
    sys.argv = ['program_name', '-i', './_ResumeInput/sample_resume.yaml', '-o', str(output_file), '-m', 'generate_pdf']
    main()  # main() will read from sys.argv

def test_output_file_generation_wordCloud(tmp_path):
    """Test if the output file is generated."""
    output_file = tmp_path / "output.png"
    sys.argv = ['program_name', '-i', './_ResumeInput/sample_resume.yaml', '-o', str(output_file), '-m', 'generate_wordcloud']
    main()  # main() will read from sys.argv
