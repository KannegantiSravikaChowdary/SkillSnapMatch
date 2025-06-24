def detect_role(text):
    role_keywords = {
        "frontend developer": ["html", "css", "javascript", "react", "figma","git"],
        "backend developer": ["node.js", "express", "sql", "flask", "django"],
        "full stack developer": [
        "html", "css", "javascript", "react", "responsive design",
        "node.js", "python", "sql", "mongodb", "api", "git"]

        "data analyst": ["python", "sql", "pandas", "excel", "tableau"],
        "ui designer": ["figma", "wireframes", "color theory", "visual hierarchy"]
    }
    text = text.lower()
    for role, skills in role_keywords.items():
        if any(skill in text for skill in skills):
            return role
    return "general"
