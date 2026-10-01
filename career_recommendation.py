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

# Store career match results
recommendations = []

# Group required skills for each career
career_skills = (
    df.groupby("career")["skill"]
    .apply(lambda skills: {
        skill.lower()
        for skill in skills
    })
)

# Compare student skills with every career
for career, required_skills in career_skills.items():

    matched_skills = student_skills.intersection(
        required_skills
    )

    missing_skills = required_skills - student_skills

    match_percentage = (
        len(matched_skills) /
        len(required_skills)
    ) * 100

    recommendations.append({
        "career": career,
        "percentage": match_percentage,
        "matched": matched_skills,
        "missing": missing_skills
    })

# Sort from highest match to lowest
recommendations.sort(
    key=lambda x: x["percentage"],
    reverse=True
)

# Display results
print("\n========== CAREER RECOMMENDATIONS ==========")

for recommendation in recommendations:

    print(
        f"\n{recommendation['career']}: "
        f"{recommendation['percentage']:.1f}%"
    )

    print("  Skills you have:")

    for skill in sorted(recommendation["matched"]):
        print("   ✓", skill.title())

    print("  Skills to learn:")

    for skill in sorted(recommendation["missing"]):
        print("   ✗", skill.title())