# Resume Builder Project

```markdown
# Resume Builder from CSV

## Overview
This project allows you to generate a professional resume from a structured CSV file. It is designed to be simple, flexible, and easy to use. The script reads data from a CSV file, organizes it by category (e.g., Skills, Education, Projects), and formats it into a clean, readable resume in **Markdown** format. The resume can then be converted into various formats like PDF or plain text.

## Features
- **CSV Input**: Store resume data in a CSV format with sections like Skills, Education, Projects, etc.
- **Customizable Sections**: Customize the order and content of resume sections.
- **Flexible Output**: Generates a resume in **Markdown** format, which can be easily converted to PDF or printed.
- **Easy to Use**: No prior programming knowledge is required to use the script.

## Requirements
- Python 3.x
- A CSV file containing your resume data (see format below)
- Optional: Conda or virtualenv for environment management

## Installation

**Clone the repository**:
   ```bash
   git clone https://github.com/your-username/resume-builder.git
   cd resume-builder
   ```

1. **Create a virtual environment** (recommended):
   If you're using `conda`, run:

   ```bash
   conda create --name resume-env python=3.11
   conda activate resume-env
   ```

   Or with `venv`:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # For Windows
   source venv/bin/activate # For macOS/Linux
   ```

2. **Install dependencies**:
   The necessary Python packages are minimal for this project. Install them using:

   ```bash
   pip install -r requirements.txt
   ```

3. **CSV Data Format**:
   Ensure your CSV file (`master_resume_content.csv`) follows this structure:

   ```csv
   Category,Title,Details
   Professional Summary,Intro,"Brief description of your professional background."
   Education,University Name,"B.S. in Computer Science, ABC University, 2023"
   Skill,Programming Languages,"Python, Java, C++"
   Project,Security App,"Developed a security application to manage passwords."
   ```

   **Note**: Each row contains a `Category` (like "Education" or "Skills"), a `Title` (like the university name or skill), and the `Details` (like the degree or a description).

## Usage

1. **Prepare your CSV file**:
   Ensure that your `master_resume_content.csv` is structured correctly as shown above and placed inside the `data/` folder.

2. **Run the Python script**:
   After setting up everything, you can generate your resume by simply running the script:

   ```bash
   python main.py
   ```

3. **View the Output**:
   The script will generate a Markdown file `generated_resume.md`. You can view it using any Markdown viewer, or convert it to PDF using a Markdown-to-PDF converter like `pandoc` or a similar tool.

4. **Customizing the Resume**:
   - You can modify the section order in the `section_order` list within `main.py`.
   - Customize the CSV format to add new sections or change existing ones.

## Advanced Features (Optional)

- **Convert to PDF**: Use libraries like `reportlab`, `weasyprint`, or `markdown-pdf` to convert your Markdown file into a PDF.
- **Web Version**: If you'd like, you can extend this project to generate HTML files or even build a web-based resume generator using Flask or Django.

## Contributing

Feel free to fork this repository, submit issues, or pull requests. I welcome improvements to the project!

## License

This project is open-source and available under the MIT License.

----
