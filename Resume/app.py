import streamlit as st
from utils.extractor import extract_text
from utils.matcher import match_resume_to_jd

st.set_page_config(page_title="Smart Resume Match", layout="centered")

st.title("🚀 Smart Resume Matcher")
st.markdown("Match your resume with job descriptions and get improvement suggestions!")

resume_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])
jd_text = st.text_area("📝 Paste the Job Description")

if st.button("Analyze"):
    if resume_file and jd_text:
        resume_text = extract_text(resume_file)
        result = match_resume_to_jd(resume_text, jd_text)

        st.subheader("🔍 Match Result")
        st.write(f"**Detected Role**: {result['role'].title()} ({result['confidence']}% confidence)")
        st.write(f"**Match Score**: {result['match_score']}%")

        st.subheader("🎓 Education Check")
        st.write(result['education_msg'])

        st.subheader("🛠️ Missing Skills")
        st.write(", ".join(result['missing_skills']) if result['missing_skills'] else "None 🎉")

        st.subheader("📚 Recommendations")
        for skill, rec in result['recommendations'].items():
            st.markdown(f"- **{skill.title()}**: {rec}")
    else:
        st.error("Please upload resume and paste job description.")

