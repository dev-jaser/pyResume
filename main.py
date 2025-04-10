import csv
from collections import defaultdict


def collect_data():
    """Collect data from the user and generate a CSV file"""
    sections = {
        "Professional Summary": "Write a brief overview of your career goals and professional background.",
        "Education": "List your education history, starting from the most recent.",
        "Skills": "List the skills you have (e.g., Python, Networking, Security).",
        "Experience": "Describe your work experience in detail (e.g., job title, company name, responsibilities).",
        "Projects": "Include personal or academic projects that showcase your skills and experience."
    }

    data = []

    # Loop through each section with guidance
    for section, guidance in sections.items():
        print(f"\n--- {section} ---")
        print(f"Guidance: {guidance}\n")

        # Ask the user to input details for each section
        if section in ["Professional Summary", "Education", "Skills"]:  # Single entry per section
            detail = input(f"Enter your {section}: ")
            data.append([section, section, detail])

        elif section == "Experience" or section == "Projects":  # Multiple entries for Experience and Projects
            print(
                f"Now enter your {section}. Type 'done' when you're finished.")
            while True:
                title = input(
                    f"Enter title for {section} (or type 'done' to finish this section): ")
                if title.lower() == 'done':
                    break
                detail = input(f"Enter details for {title}: ")
                data.append([section, title, detail])

    # Generate the CSV file after collecting all the data
    with open('resume_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Title", "Detail"])  # Write header
        writer.writerows(data)

    print("\nCSV file 'resume_data.csv' has been created!")


def load_csv(file_path):
    """Load data from a CSV file."""
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        return [row for row in reader]


def generate_resume(data):
    """Generates a resume text from CSV data."""
    resume_sections = defaultdict(list)

    # Process each row from the CSV data
    for category, title, detail in data:
        resume_sections[category].append((title, detail))

    resume_text = "# Resume\n\n"

    def format_section(title, items):
        section = f"### {title}\n"
        for item_title, item_detail in items:
            section += f'• **{item_title}** - {item_detail}\n'
        return section

    # Loop through the sections and format them
    for section_title, items in resume_sections.items():
        resume_text += format_section(section_title, items)

    return resume_text


def save_resume(resume_text, output_path):
    """Save the generated resume to a file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(resume_text)
    print(f"Resume saved as '{output_path}'")


def main():
    print("Welcome to the Interactive Resume Generator!")

    # Step 1: Collect data from the user and create the CSV
    collect_data()

    # Step 2: Load the data from the generated CSV
    file_path = 'resume_data.csv'
    data = load_csv(file_path)

    # Step 3: Generate the resume from the CSV data
    resume_text = generate_resume(data)

    # Step 4: Save the generated resume
    output_path = input(
        "Enter the output file path (e.g., generated_resume.md): ")
    save_resume(resume_text, output_path)


if __name__ == "__main__":
    main()
