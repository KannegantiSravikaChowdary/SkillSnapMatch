import re

def check_education(text, role):
    role_education_map = {
        "frontend developer": ["computer science", "information technology", "software engineering"],
        "backend developer": ["computer science", "information technology", "software engineering", "cybersecurity"],
        "full stack developer": ["computer science", "information technology", "software engineering", "cybersecurity"],
        "data analyst": ["statistics", "mathematics", "computer science", "data science"],
        "ui designer": ["design", "graphic design", "visual communication"],
        "cybersecurity analyst": ["cybersecurity", "computer science", "information technology"]
    }

    text_lower = text.lower()

    degree_patterns = r"\b(b\.tech|btech|b\.e|be|m\.tech|mtech|m\.e|me|mba|b\.sc|bsc|m\.sc|msc|mca|bca)\b"
    degrees_found = re.findall(degree_patterns, text_lower)

    field_patterns = {
        "computer science": ["computer science", "cs", "information technology", "it", "software engineering", "ai", "machine learning"],
        "statistics": ["statistics"],
        "mathematics": ["mathematics", "math"],
        "data science": ["data science"],
        "design": ["design", "graphic design", "visual communication", "animation"],
        "business": ["business", "management", "economics", "finance"],
        "cybersecurity": ["cybersecurity", "information security", "network security"]
    }

    fields_found = set()
    for core_field, variants in field_patterns.items():
        for variant in variants:
            if variant in text_lower:
                fields_found.add(core_field)

    if not degrees_found:
        return "❌ Degree not found. Please mention degree explicitly (e.g., B.Tech, M.Tech).", False

    relevant_fields = role_education_map.get(role.lower(), [])
    matched_fields = [f for f in fields_found if f in relevant_fields]

    if not matched_fields:
        return f"❌ Degree found ({', '.join(set(degrees_found))}), but no relevant field for '{role.title()}' detected.", False

    return f"✅ Degree ({', '.join(set(degrees_found))}), Field(s) ({', '.join(matched_fields)})", True
