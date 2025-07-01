import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load .env file
genai.configure(api_key="***REMOVED***")


model = genai.GenerativeModel("gemini-2.5-pro")  # or gemini-1.5-flash


def suggest_resume_improvements(missing_skills):
    if not missing_skills:
        return "✅ Your resume is strong and aligns well with the job description!"

    prompt = (
        "Given the following missing skills in a resume, suggest improvements in a professional tone.\n"
        f"Missing skills: {', '.join(missing_skills)}\n"
        "Response should be a short, actionable bullet list."
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"⚠️ Could not generate tips. Error: {str(e)}"
