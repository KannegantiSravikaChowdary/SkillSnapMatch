import fitz  # PyMuPDF
import re

# Optional: move to separate JSON or config
skills_list = [
    "python", "java", "c++", "sql", "machine learning", "data analysis",
    "tensorflow", "nlp", "react", "node.js", "mongodb", "html", "css", "javascript"
]

def extract_text_from_pdf(file):
    """Extracts and returns lowercase text from uploaded PDF."""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = "".join(page.get_text() for page in doc)
    return text.lower()

def extract_skills(text):
    """Returns list of known skills present in the text using precise word boundaries."""
    found = []
    for skill in skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)
    return found


def extract_degree(text):
    """Checks for common degree keywords."""
    return bool(re.search(r"\b(btech|b\.tech|mtech|m\.tech|bachelor|master|b\.e|m\.e)\b", text))

def calculate_match(resume_file, jd_file):
    """Calculates skill match %, matched skills, missing skills, and education match."""
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    score = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0
    edu_match = extract_degree(resume_text) and extract_degree(jd_text)

    return score, matched, missing, edu_match
