# ============================================================
# FUTURE SKILL DEMAND & CAREER RECOMMENDATION SYSTEM - 2030
# Streamlit GUI Version
# ============================================================

import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Future Career Recommendation System 2030",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CAREER DATABASE
# ============================================================

careers = {
    "Data Analyst": {
        "Python": 4, "SQL": 5, "Excel": 5,
        "Statistics": 4, "Machine Learning": 2, "Communication": 4
    },
    "Data Scientist": {
        "Python": 5, "SQL": 4, "Excel": 3,
        "Statistics": 5, "Machine Learning": 5, "Communication": 3
    },
    "Business Analyst": {
        "Python": 2, "SQL": 4, "Excel": 5,
        "Statistics": 3, "Machine Learning": 1, "Communication": 5
    },
    "Machine Learning Engineer": {
        "Python": 5, "SQL": 3, "Excel": 2,
        "Statistics": 5, "Machine Learning": 5, "Communication": 3
    },
    "Data Engineer": {
        "Python": 5, "SQL": 5, "Excel": 2,
        "Statistics": 4, "Machine Learning": 3, "Communication": 3
    },
    "AI Engineer": {
        "Python": 5, "SQL": 3, "Excel": 2,
        "Statistics": 5, "Machine Learning": 5, "Communication": 3
    },
    "Cybersecurity Analyst": {
        "Python": 3, "SQL": 3, "Excel": 3,
        "Statistics": 3, "Machine Learning": 2, "Communication": 4
    },
    "Cloud Engineer": {
        "Python": 4, "SQL": 3, "Excel": 2,
        "Statistics": 3, "Machine Learning": 2, "Communication": 4
    }
}

# ============================================================
# FUTURE DEMAND DATA (SAMPLE PROJECT SCORES)
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
    "Python": "Learn advanced Python, functions, OOP and automation.",
    "SQL": "Learn joins, subqueries, aggregate functions and window functions.",
    "Excel": "Learn Pivot Tables, VLOOKUP/XLOOKUP and advanced formulas.",
    "Statistics": "Learn probability, distributions, correlation and hypothesis testing.",
    "Machine Learning": "Learn regression, classification, clustering and model evaluation.",
    "Communication": "Improve presentation, teamwork, interview and communication skills."
}

SKILLS = ["Python", "SQL", "Excel", "Statistics", "Machine Learning", "Communication"]

# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================

if "user" not in st.session_state:
    st.session_state.user = {}

if "user_skills" not in st.session_state:
    st.session_state.user_skills = {}

if "final_scores" not in st.session_state:
    st.session_state.final_scores = {}

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def calculate_match(user_skill_data, required_skills):
    """Calculate match percentage between user skills and required skills."""
    total_score = 0
    total_skills = 0
    for skill, required_score in required_skills.items():
        user_score = user_skill_data.get(skill, 0)
        match = (user_score / required_score) * 100
        if match > 100:
            match = 100
        total_score += match
        total_skills += 1
    if total_skills == 0:
        return 0
    return total_score / total_skills


def calculate_all_career_scores():
    """Calculate skill match scores for all careers."""
    career_scores = {}
    for career, required_skills in careers.items():
        score = calculate_match(st.session_state.user_skills, required_skills)
        career_scores[career] = score
    return career_scores


def calculate_final_scores():
    """Calculate final scores (70% skill match + 30% future demand)."""
    career_scores = calculate_all_career_scores()
    final_scores = {}
    for career in careers:
        skill_score = career_scores[career]
        demand_score = future_demand[career]
        final_scores[career] = skill_score * 0.70 + demand_score * 0.30
    return final_scores


def get_top_career():
    """Get the top recommended career."""
    final_scores = calculate_final_scores()
    ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[0][0], ranked


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🎯 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Go to:",
    [
        "🏠 Home",
        "👤 Create Profile",
        "📝 Skill Assessment",
        "👁️ View Profile",
        "🏆 Career Recommendation",
        "📊 Career Ranking",
        "📉 Skill Gap Analysis",
        "🔮 Future Demand Analysis",
        "📚 Learning Roadmap",
        "📄 Generate Report",
        "ℹ️ About Project"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0 - Streamlit GUI")

# ============================================================
# PAGE: HOME
# ============================================================

if page == "🏠 Home":
    st.title("🎯 Future Skill Demand & Career Recommendation System")
    st.subheader("2030 Edition")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Available Careers", len(careers))
    with col2:
        st.metric("Skills Tracked", len(SKILLS))
    with col3:
        st.metric("Top Demand", "AI Engineer (99)")

    st.markdown("---")

    st.markdown("""
    ### 🚀 Welcome!
    
    This system analyzes your current skills and recommends careers based on:
    - **70%** Skill Compatibility
    - **30%** Future Demand Score (2030)
    
    ### 📋 How to Use
    1. **Create Profile** — Enter your basic details
    2. **Skill Assessment** — Rate your skills from 1–5
    3. **Career Recommendation** — Get personalized career suggestions
    4. **Skill Gap Analysis** — See what to improve
    5. **Learning Roadmap** — Get a personalized learning plan
    6. **Generate Report** — Download your full career analysis
    """)

    st.info("💡 **Tip:** Start by creating your profile and entering skill ratings.")


# ============================================================
# PAGE: CREATE PROFILE
# ============================================================

elif page == "👤 Create Profile":
    st.title("👤 Create Profile")
    st.markdown("---")

    with st.form("profile_form"):
        name = st.text_input("Enter your name", placeholder="e.g., John Doe")
        education = st.text_input("Enter your education", placeholder="e.g., B.Sc Computer Science")
        experience = st.number_input(
            "Enter your experience in years",
            min_value=0.0, max_value=50.0, value=0.0, step=0.5
        )
        interest = st.text_input("Enter your main interest area", placeholder="e.g., Artificial Intelligence")

        submitted = st.form_submit_button("✅ Create Profile", use_container_width=True)

        if submitted:
            if not name or not education or not interest:
                st.error("⚠️ Please fill in all fields.")
            else:
                st.session_state.user = {
                    "name": name,
                    "education": education,
                    "experience": experience,
                    "interest": interest
                }
                st.success(f"🎉 Profile created successfully for **{name}**!")
                st.balloons()

    if st.session_state.user:
        st.markdown("---")
        st.subheader("Current Profile")
        st.json(st.session_state.user)


# ============================================================
# PAGE: SKILL ASSESSMENT
# ============================================================

elif page == "📝 Skill Assessment":
    st.title("📝 Skill Assessment")
    st.markdown("---")

    if not st.session_state.user:
        st.warning("⚠️ Please create your profile first.")
        st.stop()

    st.markdown("Rate each skill from **1 (Beginner)** to **5 (Expert)**:")
    st.markdown("---")

    with st.form("skills_form"):
        skills_input = {}
        for skill in SKILLS:
            skills_input[skill] = st.slider(
                f"{skill}",
                min_value=1, max_value=5, value=3,
                help=learning.get(skill, "")
            )

        submitted = st.form_submit_button("💾 Save Skill Ratings", use_container_width=True)

        if submitted:
            st.session_state.user_skills = skills_input
            st.success("✅ Skill assessment completed!")

    if st.session_state.user_skills:
        st.markdown("---")
        st.subheader("Your Skill Ratings")
        df = pd.DataFrame(
            list(st.session_state.user_skills.items()),
            columns=["Skill", "Rating"]
        )
        st.dataframe(df, use_container_width=True, hide_index=True)


# ============================================================
# PAGE: VIEW PROFILE
# ============================================================

elif page == "👁️ View Profile":
    st.title("👁️ View Profile")
    st.markdown("---")

    if not st.session_state.user:
        st.warning("⚠️ Profile not created yet. Please create a profile first.")
        st.stop()

    user = st.session_state.user

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👤 Personal Information")
        st.write(f"**Name:** {user['name']}")
        st.write(f"**Education:** {user['education']}")
        st.write(f"**Experience:** {user['experience']} years")
        st.write(f"**Interest:** {user['interest']}")

    with col2:
        st.markdown("### 🛠️ Skill Ratings")
        if st.session_state.user_skills:
            for skill, rating in st.session_state.user_skills.items():
                st.progress(rating / 5, text=f"{skill}: {rating}/5")
        else:
            st.info("Skills not entered yet.")


# ============================================================
# PAGE: CAREER RECOMMENDATION
# ============================================================

elif page == "🏆 Career Recommendation":
    st.title("🏆 Top Career Recommendations")
    st.markdown("---")

    if not st.session_state.user_skills:
        st.warning("⚠️ Please enter your skills first.")
        st.stop()

    final_scores = calculate_final_scores()
    ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)

    top_career, _ = get_top_career()

    st.success(f"### 🎯 Recommended Career: **{top_career}**")
    st.markdown(
        "**Reason:** Your skill match and the project's future-demand "
        "score are strong for this career."
    )
    st.markdown("---")

    st.subheader("Top 5 Career Matches")

    for i, (career, score) in enumerate(ranked[:5], start=1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{i}. {career}**")
            st.progress(min(score / 100, 1.0))
        with col2:
            st.metric("Score", f"{round(score, 2)}%")

    st.markdown("---")
    st.subheader("📊 Detailed Scores")

    df = pd.DataFrame(ranked, columns=["Career", "Final Score (%)"])
    df["Final Score (%)"] = df["Final Score (%)"].round(2)
    df.index = range(1, len(df) + 1)
    st.dataframe(df, use_container_width=True)


# ============================================================
# PAGE: CAREER RANKING
# ============================================================

elif page == "📊 Career Ranking":
    st.title("📊 Career Ranking (Skill Match Only)")
    st.markdown("---")

    if not st.session_state.user_skills:
        st.warning("⚠️ Please enter your skills first.")
        st.stop()

    career_scores = calculate_all_career_scores()
    ranked = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)

    st.subheader("Ranking Based on Skill Match")

    for i, (career, score) in enumerate(ranked, start=1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{i}. {career}**")
            st.progress(min(score / 100, 1.0))
        with col2:
            st.metric("Match", f"{round(score, 2)}%")

    st.markdown("---")
    chart_data = pd.DataFrame(
        {"Career": [c for c, _ in ranked], "Score": [s for _, s in ranked]}
    )
    st.bar_chart(chart_data.set_index("Career"))


# ============================================================
# PAGE: SKILL GAP ANALYSIS
# ============================================================

elif page == "📉 Skill Gap Analysis":
    st.title("📉 Skill Gap Analysis")
    st.markdown("---")

    if not st.session_state.user_skills:
        st.warning("⚠️ Please enter your skills first.")
        st.stop()

    top_career, _ = get_top_career()
    required_skills = careers[top_career]

    st.info(f"**Target Career:** {top_career}")
    st.markdown("---")

    st.subheader("Skill Comparison")

    comparison_data = []
    for skill, required in required_skills.items():
        current = st.session_state.user_skills.get(skill, 0)
        gap = max(0, required - current)
        comparison_data.append({
            "Skill": skill,
            "Your Level": current,
            "Required": required,
            "Gap": gap,
            "Status": "✅ Met" if current >= required else "❌ Gap"
        })

    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("---")

    gaps = {row["Skill"]: row["Gap"] for row in comparison_data if row["Gap"] > 0}

    if not gaps:
        st.success("🎉 Excellent! You meet all required skill levels.")
    else:
        st.subheader("⚠️ Skills You Need to Improve")
        for skill, gap in gaps.items():
            st.warning(f"**{skill}** → Improve by **{gap}** level(s)")


# ============================================================
# PAGE: FUTURE DEMAND ANALYSIS
# ============================================================

elif page == "🔮 Future Demand Analysis":
    st.title("🔮 Future Demand Analysis — 2030")
    st.markdown("---")

    st.info(
        "📌 **NOTE:** The following are SAMPLE project scores. "
        "They should be replaced with reliable published data for a real forecast."
    )

    ranked_demand = sorted(future_demand.items(), key=lambda x: x[1], reverse=True)

    demand_data = []
    for career, score in ranked_demand:
        if score >= 95:
            level = "VERY HIGH"
        elif score >= 85:
            level = "HIGH"
        elif score >= 70:
            level = "MODERATE"
        else:
            level = "LOW"
        demand_data.append({
            "Career": career,
            "Demand Score": score,
            "Level": level
        })

    df = pd.DataFrame(demand_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("📊 Demand Visualization")

    chart_df = df.set_index("Career")["Demand Score"]
    st.bar_chart(chart_df)


# ============================================================
# PAGE: LEARNING ROADMAP
# ============================================================

elif page == "📚 Learning Roadmap":
    st.title("📚 Personalized Learning Roadmap")
    st.markdown("---")

    if not st.session_state.user_skills:
        st.warning("⚠️ Please enter your skills first.")
        st.stop()

    top_career, _ = get_top_career()
    required_skills = careers[top_career]

    st.info(f"**Target Career:** {top_career}")
    st.markdown("---")

    found_gap = False
    for skill, required in required_skills.items():
        current = st.session_state.user_skills.get(skill, 0)
        if current < required:
            found_gap = True
            with st.expander(f"📖 {skill} — Current: {current}/5 | Required: {required}/5", expanded=True):
                st.write(f"**Recommendation:** {learning.get(skill, 'Practice this skill regularly.')}")
                st.progress(current / 5, text=f"Current Level: {current}/5")
                st.progress(required / 5, text=f"Required Level: {required}/5")

    if not found_gap:
        st.success("🎉 You already meet all required skill levels!")


# ============================================================
# PAGE: GENERATE REPORT
# ============================================================

elif page == "📄 Generate Report":
    st.title("📄 Generate Career Report")
    st.markdown("---")

    if not st.session_state.user:
        st.warning("⚠️ Please create a profile first.")
        st.stop()

    if not st.session_state.user_skills:
        st.warning("⚠️ Please enter your skills first.")
        st.stop()

    if st.button("📥 Generate Report", use_container_width=True):
        user = st.session_state.user
        final_scores = calculate_final_scores()
        ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        top_career = ranked[0][0]
        required_skills = careers[top_career]

        # Build report text
        report_lines = []
        report_lines.append("=" * 70)
        report_lines.append("       FUTURE SKILL DEMAND & CAREER REPORT - 2030")
        report_lines.append("=" * 70)
        report_lines.append("")

        report_lines.append("USER PROFILE")
        report_lines.append("-" * 40)
        report_lines.append(f"Name       : {user['name']}")
        report_lines.append(f"Education  : {user['education']}")
        report_lines.append(f"Experience : {user['experience']} years")
        report_lines.append(f"Interest   : {user['interest']}")
        report_lines.append("")

        report_lines.append("CURRENT SKILLS")
        report_lines.append("-" * 40)
        for skill, rating in st.session_state.user_skills.items():
            report_lines.append(f"{skill.ljust(25)}: {rating}/5")
        report_lines.append("")

        report_lines.append("CAREER RECOMMENDATIONS")
        report_lines.append("-" * 40)
        for position, (career, score) in enumerate(ranked[:5], start=1):
            report_lines.append(f"{position}. {career} : {round(score, 2)}%")
        report_lines.append("")

        report_lines.append("TOP RECOMMENDED CAREER")
        report_lines.append("-" * 40)
        report_lines.append(f"{top_career}")
        report_lines.append(f"Future Demand Score: {future_demand[top_career]}")
        report_lines.append("")

        report_lines.append("SKILL GAP ANALYSIS")
        report_lines.append("-" * 40)
        gaps_found = False
        for skill, required in required_skills.items():
            current = st.session_state.user_skills.get(skill, 0)
            if current < required:
                gaps_found = True
                report_lines.append(
                    f"{skill} : Current {current}/5, Required {required}/5"
                )
        if not gaps_found:
            report_lines.append("No major skill gaps found.")
        report_lines.append("")

        report_lines.append("LEARNING RECOMMENDATIONS")
        report_lines.append("-" * 40)
        for skill, required in required_skills.items():
            current = st.session_state.user_skills.get(skill, 0)
            if current < required:
                report_lines.append(
                    f"{skill} -> {learning.get(skill, 'Practice this skill.')}"
                )
        report_lines.append("")
        report_lines.append("=" * 70)
        report_lines.append("End of Career Analysis Report")
        report_lines.append("=" * 70)

        report_text = "\n".join(report_lines)

        st.success("✅ Report generated successfully!")
        st.markdown("---")
        st.subheader("📄 Report Preview")
        st.text(report_text)

        st.download_button(
            label="⬇️ Download Report (career_report.txt)",
            data=report_text,
            file_name="career_report.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.markdown("---")
    st.subheader("💾 Save User Data")

    if st.button("💾 Save User Data to File", use_container_width=True):
        user = st.session_state.user
        lines = []
        lines.append("")
        lines.append("=" * 50)
        lines.append("FUTURE CAREER USER PROFILE")
        lines.append("=" * 50)
        lines.append(f"Name       : {user['name']}")
        lines.append(f"Education  : {user['education']}")
        lines.append(f"Experience : {user['experience']} years")
        lines.append(f"Interest   : {user['interest']}")
        lines.append("")
        lines.append("SKILLS")
        for skill, rating in st.session_state.user_skills.items():
            lines.append(f"{skill} : {rating}/5")
        lines.append("=" * 50)

        file_text = "\n".join(lines)
        st.download_button(
            label="⬇️ Download Users Data (users.txt)",
            data=file_text,
            file_name="users.txt",
            mime="text/plain",
            use_container_width=True
        )


# ============================================================
# PAGE: ABOUT PROJECT
# ============================================================

elif page == "ℹ️ About Project":
    st.title("ℹ️ About Project")
    st.markdown("---")

    st.markdown("""
    ### 📌 Project Name
    **Future Skill Demand & Career Recommendation System — 2030**

    ### 🎯 Purpose
    This system analyzes a user's skills and recommends careers based on
    skill compatibility and sample future-demand scores.

    ### 🛠️ Technology
    - **Python**
    - **Streamlit** (GUI)

    ### 📦 Version
    1.0 — Streamlit GUI

    ### 🧠 Main Concepts Used
    - Variables & Data Types
    - Dictionaries & Lists
    - Functions
    - Loops & Conditions
    - Session State Management
    - Sorting & Ranking
    - Data Visualization with Charts
    - File Handling (Download)
    """)

    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")