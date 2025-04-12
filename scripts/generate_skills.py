import re

# Path to the Markdown file containing skill_label calls
projects_path = "docs/projects.md"

# Path to the output skills.txt file
skills_file = "docs/skills.txt"

# Regular expression to match skill_label calls
skill_label_pattern = r'{{\s*skill_label\("([^"]+)"\)\s*}}'

def extract_skills():
    skills = []
    try:
        # Read the projects.md file
        with open(projects_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Find all skill_label calls
            matches = re.findall(skill_label_pattern, content)
            skills.extend(matches)

        # Write all extracted skills (including duplicates) to skills.txt
        with open(skills_file, "w", encoding="utf-8") as f:
            for skill in skills:
                f.write(skill + "\n")

        print(f"Extracted {len(skills)} skills to {skills_file}")
    except FileNotFoundError:
        print(f"Error: {projects_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_skills()