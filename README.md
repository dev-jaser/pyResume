# Resume Builder: Interactive Resume Generator

## Overview

The Resume Builder is a Python-based application designed to help users create a personalized resume by collecting information interactively and generating a Markdown file. This tool allows users to easily input their professional details such as summary, education, skills, experience, and projects through a guided command-line interface.

## Features

- Interactive prompts to collect resume information.
- Customizable section headers (Professional Summary, Education, Skills, Experience, Projects).
- Saves collected data in a CSV file format.
- Generates a well-structured resume in Markdown format.
- Users can modify or add more sections to suit their personal needs.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.6+ (recommended).
- `pip` or `conda` for managing dependencies.


## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/dev-jaser/pyResume.git
```

### Step 2: Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage project dependencies.

Using `venv`:

```bash
python -m venv resume-env
```

Activate the environment:

- On Windows:

  ```bash
  resume-env\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source resume-env/bin/activate
  ```

Alternatively, if you're using `conda`, you can create a new environment:

```bash
conda create --name resume-env python=3.9
conda activate resume-env
```

### Step 3: Install Dependencies

Once your environment is active, install the required dependencies:

```bash
pip install -r requirements.txt
```

If you're using Conda, ensure that all necessary dependencies are installed and available.

## How to Use

### Step 1: Run the Program

Start the program by running the following command:

```bash
python main.py
```

### Step 2: Input Your Information

The program will prompt you for the following sections:

- **Professional Summary**
- **Education**
- **Skills**
- **Experience**
- **Projects**

For each section, you will be prompted to input a title and description. If you wish to finish a section, type `done`. After collecting all information, the program will generate a CSV file (`resume_data.csv`) to store the collected data.

### Step 3: Generate the Resume

Once the data is collected, the program will generate a resume in Markdown format. You will be prompted to specify the output file path (e.g., `generated_resume.md`), where the generated resume will be saved.

## Project Structure

```plaintext
resume-builder/
│
├── main.py                 # Main program logic to generate the resume.
├── requirements.txt        # List of dependencies required to run the project.
├── resume_data.csv         # CSV file storing the collected resume data.
└── generated_resume.md     # Output file containing the generated resume in Markdown format.
```

## Customization

You can customize the resume generator by adding new sections or adjusting the format in the code. Modify the sections listed in the `collect_data()` function to fit your personal needs. Additionally, you can adjust the `generate_resume()` function to change the resume format to suit your preferences.

## Contributing

Feel free to fork the repository and submit pull requests if you have suggestions for improvements or new features. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

----
