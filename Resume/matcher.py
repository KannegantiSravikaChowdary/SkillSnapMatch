import re
from utils.education_validator import check_education

skill_db = {
    "html": "HTML Crash Course by Traversy Media",
    "css": "CSS Flexbox and Grid - Web Dev Simplified",
    "javascript": "JavaScript Mastery by Programming with Mosh",
    "react": "React Basics by Net Ninja",
    "git": "Git & GitHub - Academind",
    "responsive design": "Responsive Design: Crucial for mobile-friendly interfaces. Learn from FullstackOpen or YouTube.",
    "cybersecurity": "Cybersecurity Fundamentals - IBM Coursera or StationX",
    "node.js": "Node.js Crash Course - Traversy Media",
    "python": "Python for Everybody - Coursera",
    "sql": "SQL Basics - freeCodeCamp",
    "mongodb": "MongoDB University Free Courses"
}

roles_keywords = {
    "frontend developer": ["html", "css", "javascript", "react", "responsive design","git"],
    "backend developer": ["node.js", "python", "sql", "mongodb", "api"],
    "full stack developer": ["html", "css", "javascript", "react", "node.js", "python", "sql","api"],
    "cybersecurity analyst": ["cybersecurity", "network security", "encryption", "firewall"]
}

def detect_role(text):
    text = text.lower()
    scores = {}
    for role, keywords in roles_keywords.items():
        matches = sum(1 for kw in keywords if kw in text)
        scores[role] = matches / len(keywords)
    best_role = max(scores, key=scores.get)
    confidence = round(scores[best_role] * 100, 2)
    return best_role, confidence

def normalize(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

def match_resume_to_jd(resume_text, jd_text):
    role, confidence = detect_role(jd_text)
    required_skills = roles_keywords.get(role, [])

    normalized_resume = normalize(resume_text)
    present_skills = [skill for skill in required_skills if re.search(rf'\b{re.escape(skill)}\b', normalized_resume)]
    missing_skills = [skill for skill in required_skills if skill not in present_skills]

    match_score = round((len(present_skills) / len(required_skills)) * 100, 2) if required_skills else 0
    education_msg, _ = check_education(resume_text, role)

    recommendations = {
        skill: skill_db.get(skill, "Explore official documentation or trusted tutorials.")
        for skill in missing_skills
    }

    return {
        "role": role,
        "confidence": confidence,
        "match_score": match_score,
        "missing_skills": missing_skills,
        "recommendations": recommendations,
        "education_msg": education_msg
    }
