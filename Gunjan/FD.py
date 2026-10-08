"""
================================================================================
 FUTURE SKILL DEMAND & CAREER RECOMMENDATION SYSTEM – 2030
 Approach: Rule-Based Expert System (Zero Machine Learning)
 Techniques: Mathematical Set Theory, Weighted Jaccard Index & MCDA
 Dependencies: Pure Python (Runs directly with Standard Library)
================================================================================
"""

import sys
import json
import time

# ==============================================================================
# 1. 2030 FUTURE OF WORK & CAREER INTELLIGENCE DATASET
# ==============================================================================
CAREERS_2030_DATABASE = [
    {
        "role_id": "CR01",
        "title": "AI & Autonomous Systems Architect",
        "domain": "Artificial Intelligence & Robotics",
        "description": "Orchestrates multi-agent AI ecosystems, autonomous robotics interfaces, and edge neural systems.",
        "skills": [
            "Python", "PyTorch", "Reinforcement Learning", "Multi-Agent Systems", 
            "LLM Fine-Tuning", "Edge AI", "ROS2", "System Architecture"
        ],
        "demand_index_2030": 98,       # 1 - 100 Scale
        "growth_rate_pct": 38.5,       # Annual projected growth %
        "automation_shield": 92,       # Resistance to AI automation (1-100)
        "avg_salary_usd": 185000,
        "min_experience": "Mid"
    },
    {
        "role_id": "CR02",
        "title": "Quantum Computing Algorithm Engineer",
        "domain": "Deep Tech & Quantum",
        "description": "Develops quantum optimization routines, cryptography defenses, and molecular simulations.",
        "skills": [
            "Quantum Mechanics", "Qiskit", "Cirq", "Python", "Linear Algebra", 
            "Cryptographic Protocols", "Quantum Error Correction", "C++"
        ],
        "demand_index_2030": 94,
        "growth_rate_pct": 45.0,
        "automation_shield": 95,
        "avg_salary_usd": 210000,
        "min_experience": "Senior"
    },
    {
        "role_id": "CR03",
        "title": "AI Ethics, Governance & Safety Auditor",
        "domain": "Ethics, Legal & Tech Policy",
        "description": "Audits algorithmic bias, enforces regulatory compliance (EU AI Act), and verifies safety alignment.",
        "skills": [
            "AI Safety", "Algorithmic Auditing", "Explainable AI (XAI)", "Tech Policy", 
            "Model Interpretability", "Risk Management", "Ethical Frameworks", "Python"
        ],
        "demand_index_2030": 91,
        "growth_rate_pct": 42.0,
        "automation_shield": 97,
        "avg_salary_usd": 160000,
        "min_experience": "Entry-Mid"
    },
    {
        "role_id": "CR04",
        "title": "Cybersecurity & Post-Quantum Defense Specialist",
        "domain": "Cybersecurity",
        "description": "Secures distributed infrastructure against zero-day quantum decryption and adversarial exploits.",
        "skills": [
            "Post-Quantum Cryptography", "Zero Trust Architecture", "Cloud Security", 
            "Threat Intelligence", "Python", "Network Forensics", "Rust"
        ],
        "demand_index_2030": 96,
        "growth_rate_pct": 34.0,
        "automation_shield": 88,
        "avg_salary_usd": 175000,
        "min_experience": "Mid"
    },
    {
        "role_id": "CR05",
        "title": "Climate Tech & ESG Predictive Modeler",
        "domain": "Sustainability & Green Tech",
        "description": "Simulates planetary climate impact, carbon footprint budgets, and renewable microgrid telemetry.",
        "skills": [
            "Python", "GIS & Spatial Data", "Environmental Modeling", "Data Analysis", 
            "ESG Standards", "Time Series Forecasting", "Satellite Analytics"
        ],
        "demand_index_2030": 89,
        "growth_rate_pct": 36.0,
        "automation_shield": 90,
        "avg_salary_usd": 150000,
        "min_experience": "Entry-Mid"
    },
    {
        "role_id": "CR06",
        "title": "Synthetic Biology & Genomics Data Scientist",
        "domain": "Biotech & Healthcare",
        "description": "Applies deep computational models to genomic sequencing, protein structure prediction, and drug discovery.",
        "skills": [
            "Bioinformatics", "Python", "Genomic Sequencing", "Deep Learning", 
            "Biostatistics", "Molecular Modeling", "CRISPR Tech Principles"
        ],
        "demand_index_2030": 93,
        "growth_rate_pct": 39.0,
        "automation_shield": 93,
        "avg_salary_usd": 180000,
        "min_experience": "Mid-Senior"
    },
    {
        "role_id": "CR07",
        "title": "Spatial Computing & XR Experience Engineer",
        "domain": "Immersive Computing & XR",
        "description": "Creates holographic interfaces and industrial digital twins for collaborative enterprise workflows.",
        "skills": [
            "Unity/Unreal Engine 5", "C#", "C++", "Spatial Audio", "Computer Vision", 
            "3D Geometry", "WebXR", "HCI Design"
        ],
        "demand_index_2030": 87,
        "growth_rate_pct": 31.0,
        "automation_shield": 85,
        "avg_salary_usd": 155000,
        "min_experience": "Entry-Mid"
    },
    {
        "role_id": "CR08",
        "title": "Decentralized Finance & Smart Contract Architect",
        "domain": "FinTech & Web3",
        "description": "Architects autonomous financial protocols, cross-chain bridge security, and tokenized real-world assets.",
        "skills": [
            "Solidity", "Rust", "Smart Contract Auditing", "Cryptography", 
            "DeFi Protocols", "Distributed Systems", "Go"
        ],
        "demand_index_2030": 85,
        "growth_rate_pct": 27.5,
        "automation_shield": 82,
        "avg_salary_usd": 170000,
        "min_experience": "Mid"
    },
    {
        "role_id": "CR09",
        "title": "Neuromorphic & Edge Hardware Engineer",
        "domain": "Semiconductors & Hardware",
        "description": "Develops brain-inspired sub-milliwatt silicon chips for ambient compute and intelligent edge devices.",
        "skills": [
            "Verilog / VHDL", "VLSI Design", "Neuromorphic Architecture", "C++", 
            "FPGA Prototyping", "Embedded Systems", "Low-power Design"
        ],
        "demand_index_2030": 92,
        "growth_rate_pct": 33.0,
        "automation_shield": 94,
        "avg_salary_usd": 190000,
        "min_experience": "Senior"
    },
    {
        "role_id": "CR10",
        "title": "Smart City IoT & Renewable Grid Engineer",
        "domain": "IoT & Infrastructure",
        "description": "Integrates connected sensor telemetry, distributed solar-wind microgrids, and automated municipal systems.",
        "skills": [
            "IoT Architecture", "MQTT / SCADA Protocols", "Python", "Power Systems", 
            "Cloud Infrastructure", "Cyber-Physical Systems", "Kafka"
        ],
        "demand_index_2030": 88,
        "growth_rate_pct": 32.5,
        "automation_shield": 89,
        "avg_salary_usd": 145000,
        "min_experience": "Entry-Mid"
    }
]

# ==============================================================================
# 2. RULE-BASED EXPERT ENGINE (SET THEORY & MCDA)
# ==============================================================================
SKILL_TIER_WEIGHTS = {
    "reinforcement learning": 3.0, "quantum mechanics": 3.0, "qiskit": 3.0,
    "post-quantum cryptography": 3.0, "ai safety": 3.0, "synthetic biology": 3.0,
    "zero trust architecture": 2.5, "multi-agent systems": 2.5, "llm fine-tuning": 2.5,
    "explainable ai (xai)": 2.5, "bioinformatics": 2.5, "neuromorphic architecture": 2.5,
    "pytorch": 2.0, "c++": 2.0, "rust": 2.0, "solidity": 2.0, "unity/unreal engine 5": 2.0,
    "python": 1.5, "r": 1.5, "c#": 1.5, "go": 1.5, "linux": 1.0, "sql": 1.0
}
DEFAULT_SKILL_WEIGHT = 1.5

def get_skill_weight(skill_name):
    return SKILL_TIER_WEIGHTS.get(skill_name.strip().lower(), DEFAULT_SKILL_WEIGHT)

def calculate_weighted_jaccard(user_skills, role_skills):
    """Calculates deterministic Weighted Jaccard skill coverage using set theory."""
    user_set = set(s.strip().lower() for s in user_skills)
    
    total_role_weight = 0.0
    matched_weight = 0.0
    acquired_skills = []
    missing_skills = []
    
    for s in role_skills:
        w = get_skill_weight(s)
        total_role_weight += w
        if s.strip().lower() in user_set:
            matched_weight += w
            acquired_skills.append(s)
        else:
            missing_skills.append(s)
            
    coverage_ratio = (matched_weight / total_role_weight) if total_role_weight > 0 else 0.0
    return coverage_ratio, acquired_skills, missing_skills

def evaluate_careers(user_skills, experience_tier="Student / Fresher", target_domain=None):
    """
    Multi-Criteria Decision Analysis (MCDA - Weighted Sum Model)
    Criteria:
      - Skill Coverage: 45%
      - 2030 Demand Index: 25%
      - Projected Growth Rate: 15%
      - Automation Shield: 15%
    """
    recommendations = []
    
    for role in CAREERS_2030_DATABASE:
        if target_domain and target_domain.lower() != "all" and target_domain.lower() not in role["domain"].lower():
            continue
            
        coverage_ratio, acquired, missing = calculate_weighted_jaccard(user_skills, role["skills"])
        
        norm_demand = role["demand_index_2030"] / 100.0
        norm_growth = min(role["growth_rate_pct"] / 50.0, 1.0)
        norm_shield = role["automation_shield"] / 100.0
        
        # Experience multiplier rule
        exp_multiplier = 1.0
        if "Senior" in role["min_experience"] and "Student" in experience_tier:
            exp_multiplier = 0.88
        elif "Entry" in role["min_experience"] and "Student" in experience_tier:
            exp_multiplier = 1.05
            
        composite_score = (
            (0.45 * coverage_ratio) + 
            (0.25 * norm_demand) + 
            (0.15 * norm_growth) + 
            (0.15 * norm_shield)
        ) * 100.0 * exp_multiplier
        
        recommendations.append({
            "title": role["title"],
            "domain": role["domain"],
            "composite_score": round(min(composite_score, 100.0), 1),
            "skill_coverage_pct": round(coverage_ratio * 100.0, 1),
            "demand_index": role["demand_index_2030"],
            "growth_rate_pct": role["growth_rate_pct"],
            "automation_shield": role["automation_shield"],
            "avg_salary_usd": role["avg_salary_usd"],
            "acquired_skills": acquired,
            "missing_skills": missing,
            "all_skills": role["skills"],
            "description": role["description"]
        })
        
    recommendations.sort(key=lambda x: x["composite_score"], reverse=True)
    return recommendations

def generate_roadmap(missing_skills, role_title):
    """Generates a 3-phase prerequisite-ordered roadmap."""
    if not missing_skills:
        return [
            ("Phase 1: Portfolio Readiness (Months 1-3)", ["Open Source Documentation"], "Publish complete 2030 project repository."),
            ("Phase 2: Vanguard Deployment (Months 4-6)", ["Industry Benchmark Capstone"], "Deploy live operational prototype.")
        ]
        
    sorted_skills = sorted(missing_skills, key=lambda s: get_skill_weight(s))
    n = len(sorted_skills)
    p1 = sorted_skills[:max(1, n // 3)]
    p2 = sorted_skills[len(p1):len(p1) + max(1, (n - len(p1)) // 2)]
    p3 = sorted_skills[len(p1) + len(p2):] or [sorted_skills[-1]]
    
    return [
        ("Phase 1: Core Toolchains & Principles (Months 1-3)", p1, f"Master foundational syntax and theory for {', '.join(p1)}."),
        ("Phase 2: Applied 2030 Engineering (Months 4-6)", p2, f"Build production-grade simulation pipelines using {', '.join(p2)}."),
        ("Phase 3: Vanguard Enterprise Capstone (Months 7-9)", p3, f"Deliver a live real-world solution for {role_title} using {', '.join(p3)}.")
    ]

# ==============================================================================
# 3. CONSOLE VISUALIZATION HELPERS
# ==============================================================================
def draw_bar(value, max_val=100, length=20):
    filled = int(round((value / max_val) * length))
    return "█" * filled + "░" * (length - filled)

def print_header(title):
    print("\n" + "=" * 78)
    print(f" {title}")
    print("=" * 78)

# ==============================================================================
# 4. MAIN INTERACTIVE EXECUTION
# ==============================================================================
def main():
    print_header("🔮 FUTURE SKILL DEMAND & CAREER RECOMMENDATION SYSTEM – 2030\n    [ Rule-Based Expert System • Set Theory & MCDA • No ML ]")
    
    print("\nSelect an option to run:")
    print(" 1. Run with Sample Profile (CS Student: Python, C++, Data Analysis, Linux)")
    print(" 2. Enter My Own Custom Skills & Experience")
    choice = input("\nEnter choice [1 or 2, default=1]: ").strip()
    
    if choice == "2":
        print("\nEnter your current skills separated by commas.")
        print("Examples: Python, C++, Rust, PyTorch, AI Safety, Cloud Security, Qiskit, Solidity")
        user_skills_raw = input("\nYour Skills: ").strip()
        user_skills = [s.strip() for s in user_skills_raw.split(",") if s.strip()] if user_skills_raw else ["Python", "C++"]
        
        print("\nSelect Experience Tier:")
        print(" 1. Student / Fresher (0-1 yrs)")
        print(" 2. Junior Developer (1-3 yrs)")
        print(" 3. Mid-Senior Specialist (3+ yrs)")
        exp_input = input("Tier [1-3, default=1]: ").strip()
        exp_map = {"1": "Student / Fresher", "2": "Junior Developer", "3": "Mid-Senior Specialist"}
        experience_tier = exp_map.get(exp_input, "Student / Fresher")
    else:
        user_skills = ["Python", "C++", "Data Analysis", "Linux"]
        experience_tier = "Student / Fresher"
        print(f"\n✓ Loaded Sample Profile: {', '.join(user_skills)} ({experience_tier})")
        
    print("\nEvaluating 2030 job market matrices using Weighted Jaccard & MCDA...")
    time.sleep(0.5)
    
    results = evaluate_careers(user_skills, experience_tier)
    
    # Display Top 5 Career Pathways
    print_header("🏆 TOP RECOMMENDED 2030 CAREER PATHWAYS")
    for rank, res in enumerate(results[:5], 1):
        print(f"\n#{rank}. {res['title'].upper()}")
        print(f"    Domain:                {res['domain']}")
        print(f"    Composite Fit (MCDA):  {draw_bar(res['composite_score'])} {res['composite_score']}%")
        print(f"    Skill Match Coverage:  {draw_bar(res['skill_coverage_pct'])} {res['skill_coverage_pct']}%")
        print(f"    2030 Demand Index:     {res['demand_index']}/100")
        print(f"    AI Automation Shield:  {res['automation_shield']}% (Resistance to replacement)")
        print(f"    Avg Projected Salary:  ${res['avg_salary_usd']:,}/yr")
        print(f"    Acquired Skills:       {', '.join(res['acquired_skills']) if res['acquired_skills'] else 'None'}")
        print(f"    Missing 2030 Skills:   {', '.join(res['missing_skills'])}")
        
    # Top Choice Roadmap
    top_career = results[0]
    roadmap = generate_roadmap(top_career["missing_skills"], top_career["title"])
    
    print_header(f"🗺️ PREREQUISITE-ORDERED ROADMAP FOR: {top_career['title']}")
    for phase_name, skills_to_learn, action_desc in roadmap:
        print(f"\n📌 {phase_name}")
        print(f"   • Skills to Master: {', '.join(skills_to_learn)}")
        print(f"   • Action Plan:      {action_desc}")
        
    # Save Report Option
    print("\n" + "-" * 78)
    save_opt = input("Would you like to export your 2030 Career Diagnostic Report? (y/n): ").strip().lower()
    if save_opt == "y":
        filename = "career_2030_report.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write("FUTURE SKILL DEMAND & CAREER REPORT – 2030\n")
            f.write("=" * 60 + "\n")
            f.write(f"User Skills: {', '.join(user_skills)}\n")
            f.write(f"Experience Tier: {experience_tier}\n\n")
            f.write("TOP RECOMMENDED 2030 PATHWAYS:\n")
            for r in results[:5]:
                f.write(f"- {r['title']} (Fit: {r['composite_score']}%, Demand: {r['demand_index']}/100, Salary: ${r['avg_salary_usd']:,})\n")
                f.write(f"  Missing Skills: {', '.join(r['missing_skills'])}\n\n")
            f.write("UPSKILLING ROADMAP:\n")
            for p, sk, act in roadmap:
                f.write(f"{p}\n  Skills: {', '.join(sk)}\n  Action: {act}\n\n")
        print(f"✓ Report successfully generated and saved to: {filename}")
        
    print("\nThank you for using Future Skill Demand & Career Recommendation System – 2030!\n")

if __name__ == "__main__":
    main()