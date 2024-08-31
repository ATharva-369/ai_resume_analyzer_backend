# AI-Powered Resume Analyzer

## Overview

The AI-Powered Resume Analyzer is a Python-based tool designed to analyze resumes, extract key information such as skills, and perform a Job Description Matching and Skill Gap Analysis. This tool is ideal for both job seekers and recruiters, helping to quickly identify how well a candidate's resume matches a job description and what skills might be missing. Its a working proof of my skills and a little something I made when I was bored.

## Features

- **Resume Parsing:** Extracts skills, roles, and company names from resumes in PDF format.
- **Skill Normalization:** Matches and normalizes extracted skills using spaCy's NLP capabilities.
- **Job Description Matching:** Compares extracted resume skills with those required in job descriptions.
- **Skill Gap Analysis:** Identifies and reports on missing skills that the candidate needs to meet the job requirements.
- **JSON Output:** Saves the parsed and analyzed data in a structured JSON format.
- **Three Types Of Scores:** It uses Gemini, the data parsed and a NLP model to find matching patterns. It generates an individual resume score, a compatibility summary and a compability score.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install Required Python Packages

```bash
pip install -r requirements.txt
```
### Get API key
- Get an API key from <a href="https://aistudio.google.com/app/apikey">here</a>.
- Create an .env file in the same directory and put this in the file: **API_KEY = YOUR API KEY**

## Usage
- Run **main.py**
- Input the path of the resume's **OCR** pdf.
- Paste in the job description
- A markdown file will be generated with the scores and analysis. Use <a href="https://markdownlivepreview.com/">this website</a> to paste in and view the markdown file.
