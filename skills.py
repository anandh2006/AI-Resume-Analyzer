def extract_skills(text):
    keywords = [
        "Python", "Java", "SQL", "HTML", "CSS", "JavaScript",
        "React", "Node.js", "Pandas", "NumPy", "Power BI", "Tableau",
        "Data Analysis", "Machine Learning", "Deep Learning", "NLP", "TensorFlow"
    ]
    extracted = [skill for skill in keywords if skill.lower() in text.lower()]
    return extracted

def match_jobs(extracted_skills):
    job_roles = {
        "Data Analyst": ["Python", "SQL", "Data Analysis", "Pandas", "Power BI"],
        "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Bootstrap"],
        "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "NLP"]
    }

    matched_roles = []

    for title, required_skills in job_roles.items():
        matched = [skill for skill in required_skills if skill in extracted_skills]
        missing = [skill for skill in required_skills if skill not in extracted_skills]
        score = round(len(matched) / len(required_skills) * 100) if required_skills else 0

        matched_roles.append({
            "title": title,
            "score": score,
            "missing_skills": missing
        })

    return matched_roles
