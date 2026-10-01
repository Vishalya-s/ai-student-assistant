import pandas as pd

# Load career-skill data
df = pd.read_csv("career_data/career_skills.csv")

# Get student's skills
student_input = input(
    "Enter your skills separated by commas: "
)

student_skills = {
    skill.strip().lower()
    for skill in student_input.split(",")
}

# Get career
career = input("Enter your target career: ")

# Find required skills
career_data = df[
    df["career"].str.lower() == career.strip().lower()
]

if career_data.empty:
    print("\nCareer not found.")
else:
    required_skills = {
        skill.lower()
        for skill in career_data["skill"]
    }

    # Find matching and missing skills
    matched_skills = student_skills.intersection(required_skills)
    missing_skills = required_skills - student_skills

    print("\n========== SKILL GAP ANALYSIS ==========")

    print("\nSkills you already have:")
    for skill in sorted(matched_skills):
        print("✓", skill.title())

    print("\nSkills you need to learn:")
    for skill in sorted(missing_skills):
        print("✗", skill.title())

    # Calculate percentage
    if required_skills:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100

        print(
            f"\nSkill Match: {match_percentage:.1f}%"
        )