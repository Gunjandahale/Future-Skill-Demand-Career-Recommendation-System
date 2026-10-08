# ============================================================
# FUTURE SKILL DEMAND & CAREER RECOMMENDATION SYSTEM - 2030
# Version 1 - Basic Python Project
# ============================================================


# ============================================================
# CAREER DATABASE
# ============================================================

careers = {

    "Data Analyst": {
        "Python": 4,
        "SQL": 5,
        "Excel": 5,
        "Statistics": 4,
        "Machine Learning": 2,
        "Communication": 4
    },

    "Data Scientist": {
        "Python": 5,
        "SQL": 4,
        "Excel": 3,
        "Statistics": 5,
        "Machine Learning": 5,
        "Communication": 3
    },

    "Business Analyst": {
        "Python": 2,
        "SQL": 4,
        "Excel": 5,
        "Statistics": 3,
        "Machine Learning": 1,
        "Communication": 5
    },

    "Machine Learning Engineer": {
        "Python": 5,
        "SQL": 3,
        "Excel": 2,
        "Statistics": 5,
        "Machine Learning": 5,
        "Communication": 3
    },

    "Data Engineer": {
        "Python": 5,
        "SQL": 5,
        "Excel": 2,
        "Statistics": 4,
        "Machine Learning": 3,
        "Communication": 3
    },

    "AI Engineer": {
        "Python": 5,
        "SQL": 3,
        "Excel": 2,
        "Statistics": 5,
        "Machine Learning": 5,
        "Communication": 3
    },

    "Cybersecurity Analyst": {
        "Python": 3,
        "SQL": 3,
        "Excel": 3,
        "Statistics": 3,
        "Machine Learning": 2,
        "Communication": 4
    },

    "Cloud Engineer": {
        "Python": 4,
        "SQL": 3,
        "Excel": 2,
        "Statistics": 3,
        "Machine Learning": 2,
        "Communication": 4
    }
}


# ============================================================
# FUTURE DEMAND DATA
# NOTE:
# These are SAMPLE PROJECT SCORES, not real 2030 forecasts.
# ============================================================

future_demand = {

    "Data Analyst": 85,
    "Data Scientist": 95,
    "Business Analyst": 82,
    "Machine Learning Engineer": 98,
    "Data Engineer": 96,
    "AI Engineer": 99,
    "Cybersecurity Analyst": 94,
    "Cloud Engineer": 93
}


# ============================================================
# LEARNING RECOMMENDATIONS
# ============================================================

learning = {

    "Python":
        "Learn advanced Python, functions, OOP and automation.",

    "SQL":
        "Learn joins, subqueries, aggregate functions and window functions.",

    "Excel":
        "Learn Pivot Tables, VLOOKUP/XLOOKUP and advanced formulas.",

    "Statistics":
        "Learn probability, distributions, correlation and hypothesis testing.",

    "Machine Learning":
        "Learn regression, classification, clustering and model evaluation.",

    "Communication":
        "Improve presentation, teamwork, interview and communication skills."
}


# ============================================================
# GLOBAL VARIABLES
# ============================================================

user = {}

user_skills = {}

career_scores = {}

final_scores = {}

ranked_careers = []


# ============================================================
# FUNCTION 1: CREATE PROFILE
# ============================================================

def create_profile():

    print("\n")
    print("=" * 55)
    print("                 CREATE PROFILE")
    print("=" * 55)

    user["name"] = input("Enter your name: ")

    user["education"] = input("Enter your education: ")

    while True:

        try:
            experience = float(
                input("Enter your experience in years: ")
            )

            if experience < 0:
                print("Experience cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    user["experience"] = experience

    user["interest"] = input(
        "Enter your main interest area: "
    )

    print("\nProfile created successfully!")


# ============================================================
# FUNCTION 2: ENTER SKILLS
# ============================================================

def enter_skills():

    global user_skills

    if not user:

        print("\nPlease create your profile first.")

        return

    print("\n")
    print("=" * 55)
    print("                  SKILL ASSESSMENT")
    print("=" * 55)

    skills = [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Machine Learning",
        "Communication"
    ]

    user_skills = {}

    for skill in skills:

        while True:

            try:

                rating = int(
                    input(
                        "Rate your " +
                        skill +
                        " skill (1-5): "
                    )
                )

                if rating < 1 or rating > 5:

                    print(
                        "Please enter a rating between 1 and 5."
                    )

                else:

                    user_skills[skill] = rating
                    break

            except ValueError:

                print("Please enter a number from 1 to 5.")

    print("\nSkill assessment completed!")


# ============================================================
# FUNCTION 3: VIEW PROFILE
# ============================================================

def view_profile():

    print("\n")
    print("=" * 55)
    print("                    USER PROFILE")
    print("=" * 55)

    if not user:

        print("Profile not created yet.")

        return

    print("Name       :", user["name"])
    print("Education  :", user["education"])
    print("Experience :", user["experience"], "years")
    print("Interest   :", user["interest"])

    print("\nSkills")
    print("-" * 40)

    if not user_skills:

        print("Skills not entered yet.")

    else:

        for skill, rating in user_skills.items():

            print(
                skill.ljust(20),
                ":",
                rating,
                "/ 5"
            )


# ============================================================
# FUNCTION 4: CALCULATE SKILL MATCH
# ============================================================

def calculate_match(user_skill_data, required_skills):

    total_score = 0
    total_skills = 0

    for skill, required_score in required_skills.items():

        user_score = user_skill_data.get(skill, 0)

        match = (
            user_score / required_score
        ) * 100

        if match > 100:
            match = 100

        total_score += match

        total_skills += 1

    if total_skills == 0:

        return 0

    return total_score / total_skills


# ============================================================
# FUNCTION 5: CALCULATE CAREER SCORES
# ============================================================

def calculate_all_career_scores():

    global career_scores

    career_scores = {}

    for career, required_skills in careers.items():

        score = calculate_match(
            user_skills,
            required_skills
        )

        career_scores[career] = score


# ============================================================
# FUNCTION 6: CAREER RANKING
# ============================================================

def rank_careers():

    global ranked_careers

    if not user_skills:

        print("\nPlease enter your skills first.")

        return

    calculate_all_career_scores()

    ranked_careers = sorted(
        career_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n")
    print("=" * 60)
    print("                  CAREER RANKING")
    print("=" * 60)

    position = 1

    for career, score in ranked_careers:

        print(
            str(position) +
            ". " +
            career.ljust(28) +
            str(round(score, 2)) +
            "%"
        )

        position += 1


# ============================================================
# FUNCTION 7: FINAL CAREER SCORE
# ============================================================

def calculate_final_scores():

    global final_scores

    calculate_all_career_scores()

    final_scores = {}

    for career in careers:

        skill_score = career_scores[career]

        demand_score = future_demand[career]

        # 70% skill match
        # 30% future demand

        final_score = (
            skill_score * 0.70
            +
            demand_score * 0.30
        )

        final_scores[career] = final_score


# ============================================================
# FUNCTION 8: CAREER RECOMMENDATION
# ============================================================

def recommend_career():

    if not user_skills:

        print("\nPlease enter your skills first.")

        return

    calculate_final_scores()

    ranked = sorted(
        final_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n")
    print("=" * 65)
    print("             TOP CAREER RECOMMENDATIONS")
    print("=" * 65)

    position = 1

    for career, score in ranked[:5]:

        print(
            str(position) +
            ". " +
            career.ljust(30) +
            str(round(score, 2)) +
            "%"
        )

        position += 1

    top_career = ranked[0][0]

    print("\nRecommended Career:")
    print(">>>", top_career)

    print(
        "Reason: Your skill match and the project's "
        "future-demand score are strong for this career."
    )


# ============================================================
# FUNCTION 9: SKILL GAP ANALYSIS
# ============================================================

def skill_gap_analysis():

    if not user_skills:

        print("\nPlease enter your skills first.")

        return

    calculate_final_scores()

    ranked = sorted(
        final_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_career = ranked[0][0]

    required_skills = careers[top_career]

    print("\n")
    print("=" * 65)
    print("                  SKILL GAP ANALYSIS")
    print("=" * 65)

    print("Target Career:", top_career)

    print("\n")
    print(
        "Skill".ljust(25),
        "Your Level".ljust(15),
        "Required"
    )

    print("-" * 60)

    gaps = {}

    for skill, required in required_skills.items():

        current = user_skills.get(skill, 0)

        print(
            skill.ljust(25),
            str(current).ljust(15),
            required
        )

        if current < required:

            gaps[skill] = required - current

    print("\n")

    if not gaps:

        print("Excellent! You meet all required skill levels.")

    else:

        print("Skills You Need to Improve:")
        print("-" * 40)

        for skill, gap in gaps.items():

            print(
                skill +
                " -> Improve by " +
                str(gap) +
                " level(s)"
            )


# ============================================================
# FUNCTION 10: FUTURE DEMAND
# ============================================================

def show_future_demand():

    print("\n")
    print("=" * 65)
    print("             FUTURE DEMAND ANALYSIS - 2030")
    print("=" * 65)

    print(
        "\nNOTE: The following are SAMPLE project scores."
    )

    print(
        "They should be replaced with reliable published "
        "data for a real forecast.\n"
    )

    ranked_demand = sorted(
        future_demand.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for career, score in ranked_demand:

        if score >= 95:

            level = "VERY HIGH"

        elif score >= 85:

            level = "HIGH"

        elif score >= 70:

            level = "MODERATE"

        else:

            level = "LOW"

        print(
            career.ljust(30),
            str(score).ljust(8),
            level
        )


# ============================================================
# FUNCTION 11: LEARNING RECOMMENDATION
# ============================================================

def learning_recommendation():

    if not user_skills:

        print("\nPlease enter your skills first.")

        return

    calculate_final_scores()

    ranked = sorted(
        final_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_career = ranked[0][0]

    required_skills = careers[top_career]

    print("\n")
    print("=" * 65)
    print("             PERSONALIZED LEARNING ROADMAP")
    print("=" * 65)

    print("Target Career:", top_career)

    print("\nRecommended Skills:\n")

    found_gap = False

    for skill, required in required_skills.items():

        current = user_skills.get(skill, 0)

        if current < required:

            found_gap = True

            print("Skill:", skill)

            print(
                "Current Level :",
                current,
                "/ 5"
            )

            print(
                "Required Level:",
                required,
                "/ 5"
            )

            print(
                "Recommendation:",
                learning.get(
                    skill,
                    "Practice this skill regularly."
                )
            )

            print("-" * 55)

    if not found_gap:

        print(
            "You already meet all required skill levels!"
        )


# ============================================================
# FUNCTION 12: SAVE USER DATA
# ============================================================

def save_user_data():

    if not user:

        print("\nPlease create a profile first.")

        return

    try:

        with open(
            "users.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write("\n")
            file.write("=" * 50 + "\n")

            file.write(
                "FUTURE CAREER USER PROFILE\n"
            )

            file.write("=" * 50 + "\n")

            file.write(
                "Name       : " +
                user["name"] +
                "\n"
            )

            file.write(
                "Education  : " +
                user["education"] +
                "\n"
            )

            file.write(
                "Experience : " +
                str(user["experience"]) +
                " years\n"
            )

            file.write(
                "Interest   : " +
                user["interest"] +
                "\n"
            )

            file.write("\nSKILLS\n")

            for skill, rating in user_skills.items():

                file.write(
                    skill +
                    " : " +
                    str(rating) +
                    "/5\n"
                )

            file.write("=" * 50 + "\n")

        print(
            "\nUser data saved successfully to users.txt"
        )

    except Exception as error:

        print(
            "Error while saving data:",
            error
        )


# ============================================================
# FUNCTION 13: GENERATE CAREER REPORT
# ============================================================

def generate_report():

    if not user:

        print("\nPlease create a profile first.")

        return

    if not user_skills:

        print("\nPlease enter your skills first.")

        return

    calculate_final_scores()

    ranked = sorted(
        final_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_career = ranked[0][0]

    required_skills = careers[top_career]

    try:

        with open(
            "career_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("=" * 70 + "\n")
            file.write(
                "       FUTURE SKILL DEMAND & CAREER REPORT - 2030\n"
            )
            file.write("=" * 70 + "\n\n")

            # Profile

            file.write("USER PROFILE\n")
            file.write("-" * 40 + "\n")

            file.write(
                "Name       : " +
                user["name"] +
                "\n"
            )

            file.write(
                "Education  : " +
                user["education"] +
                "\n"
            )

            file.write(
                "Experience : " +
                str(user["experience"]) +
                " years\n"
            )

            file.write(
                "Interest   : " +
                user["interest"] +
                "\n\n"
            )

            # Skills

            file.write("CURRENT SKILLS\n")
            file.write("-" * 40 + "\n")

            for skill, rating in user_skills.items():

                file.write(
                    skill.ljust(25) +
                    ": " +
                    str(rating) +
                    "/5\n"
                )

            file.write("\n")

            # Career Ranking

            file.write("CAREER RECOMMENDATIONS\n")
            file.write("-" * 40 + "\n")

            for position, (career, score) in enumerate(
                ranked[:5],
                start=1
            ):

                file.write(
                    str(position) +
                    ". " +
                    career +
                    " : " +
                    str(round(score, 2)) +
                    "%\n"
                )

            file.write("\n")

            # Top Career

            file.write("TOP RECOMMENDED CAREER\n")
            file.write("-" * 40 + "\n")

            file.write(
                top_career +
                "\n"
            )

            file.write(
                "Future Demand Score: " +
                str(future_demand[top_career]) +
                "\n\n"
            )

            # Skill Gap

            file.write("SKILL GAP ANALYSIS\n")
            file.write("-" * 40 + "\n")

            gaps_found = False

            for skill, required in required_skills.items():

                current = user_skills.get(skill, 0)

                if current < required:

                    gaps_found = True

                    file.write(
                        skill +
                        " : Current " +
                        str(current) +
                        "/5, Required " +
                        str(required) +
                        "/5\n"
                    )

            if not gaps_found:

                file.write(
                    "No major skill gaps found.\n"
                )

            file.write("\n")

            # Learning Roadmap

            file.write("LEARNING RECOMMENDATIONS\n")
            file.write("-" * 40 + "\n")

            for skill, required in required_skills.items():

                current = user_skills.get(skill, 0)

                if current < required:

                    file.write(
                        skill +
                        " -> " +
                        learning.get(
                            skill,
                            "Practice this skill."
                        ) +
                        "\n"
                    )

            file.write("\n")

            file.write("=" * 70 + "\n")
            file.write(
                "End of Career Analysis Report\n"
            )
            file.write("=" * 70 + "\n")

        print(
            "\nCareer report generated successfully!"
        )

        print(
            "File: career_report.txt"
        )

    except Exception as error:

        print(
            "Error while generating report:",
            error
        )


# ============================================================
# FUNCTION 14: ABOUT PROJECT
# ============================================================

def about_project():

    print("\n")
    print("=" * 65)
    print("                     ABOUT PROJECT")
    print("=" * 65)

    print("""
Project Name:
Future Skill Demand & Career Recommendation System - 2030

Purpose:
This system analyzes a user's skills and recommends
careers based on skill compatibility and sample
future-demand scores.

Technology:
Python

Version:
1.0 - Basic Python

Main Concepts Used:
- Variables
- Dictionaries
- Lists
- Functions
- Loops
- Conditions
- File Handling
- Sorting
- Exception Handling
""")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 65)
        print("      FUTURE SKILL DEMAND & CAREER RECOMMENDATION")
        print("                         2030")
        print("=" * 65)

        print("1.  Create Profile")
        print("2.  Enter Skill Ratings")
        print("3.  View Profile")
        print("4.  Career Recommendation")
        print("5.  Career Ranking")
        print("6.  Skill Gap Analysis")
        print("7.  Future Demand Analysis")
        print("8.  Learning Recommendation")
        print("9.  Save User Data")
        print("10. Generate Career Report")
        print("11. About Project")
        print("12. Exit")

        print("-" * 65)

        choice = input(
            "Enter your choice (1-12): "
        )

        if choice == "1":

            create_profile()

        elif choice == "2":

            enter_skills()

        elif choice == "3":

            view_profile()

        elif choice == "4":

            recommend_career()

        elif choice == "5":

            rank_careers()

        elif choice == "6":

            skill_gap_analysis()

        elif choice == "7":

            show_future_demand()

        elif choice == "8":

            learning_recommendation()

        elif choice == "9":

            save_user_data()

        elif choice == "10":

            generate_report()

        elif choice == "11":

            about_project()

        elif choice == "12":

            print("\nThank you for using the system!")

            print(
                "Good luck with your future career!"
            )

            break

        else:

            print(
                "\nInvalid choice!"
            )

            print(
                "Please enter a number between 1 and 12."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()
    