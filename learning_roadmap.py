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

# Get target career
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

    # Find missing skills
    missing_skills = required_skills - student_skills

    print("\n========== PERSONALIZED LEARNING ROADMAP ==========")

    if not missing_skills:
        print("\nYou already have all the required skills!")
    else:
        print("\nSkills you should learn:")

        for number, skill in enumerate(
            sorted(missing_skills), start=1
        ):
            print(f"{number}. {skill.title()}")

        print("\nRecommended order:")

        roadmap_order = [
            "python",
            "mathematics",
            "statistics",
            "sql",
            "machine learning",
            "tensorflow",
            "deep learning",
            "git",
            "data structures",
            "algorithms",
            "javascript",
            "react",
            "spring boot",
            "rest api"
        ]

        step = 1

        for skill in roadmap_order:
            if skill in missing_skills:
                print(
                    f"Step {step}: Learn {skill.title()}"
                )
                step += 1