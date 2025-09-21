from pathlib import Path
import os

root = Path(__file__).parent.parent

TEMPLATE_ITEMS = ["Milestones.md", "Reading.md", "References.md", "Tasks.md", "Roadmap.md"]

def write_readme_content(readme_path):
    pass

def make_work_item(name):
    """ Create the files and folders for a new work item. """
    # Make the root for the work item (project/Discipline)
    os.makedirs(root / "Work" / name, exist_ok=True)

    # Make the 'Dive/' folder 
    os.makedirs(root / "Work" / name / "Dive", exist_ok=True)

    # Make the template files
    for item in TEMPLATE_ITEMS:
        with open(root / "Work" / name / "Dive"/ item, "w") as f:
            f.write(" ")

    # Make the Readme.md file
    with open(root / "Work" / name / "Readme.md", "w") as f:
        f.write(" ")

if __name__ == "__main__":
    name = input("Enter the name of the project/Discipline (e.g. P-Project1, D-Discipline1): ")
    make_work_item(name)
