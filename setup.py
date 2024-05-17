from setuptools import setup, find_packages

setup(
    name='resumeConvertFromYAML',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'argparse',
        'nltk',
        'python-docx',
        'PyYAML',
        'reportlab',
        'scikit-learn',
        'sentence-transformers',
        'spacy',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'resumeConvertFromYAML=resumeConvertFromYAML.process_data:main'
        ],
    },
)
