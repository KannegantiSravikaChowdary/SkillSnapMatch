import streamlit as st
from matcher import calculate_match
from enhancer import suggest_resume_improvements

st.set_page_config(page_title="Smart Resume Match", layout="centered")

# --- Header Section ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 42px;'>📄 Smart Resume Match</h1>
        <p style='font-size: 18px; color: #5a5a5a;'>
            Match resumes with job descriptions using <b>AI</b>, <b>NLP</b>, and smart skill analysis.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Upload Section (One Below the Other) ---
# Custom CSS: Bigger boxes + spacing
st.markdown("""
    <style>
    .stFileUploader {
        padding: 1.5rem !important;
        height: 200px !important;
        border: 2.5px solid #d3d3d3;
        border-radius: 15px;
        background-color: #fafafa;
    }
    section.main > div {
        padding-top: 15px !important;
        padding-bottom: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
st.markdown("#### 📤 Upload Resume (PDF)")
resume_file = st.file_uploader("Resume", type=["pdf"], key="resume", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
st.markdown("#### 📥 Upload Job Description (PDF)")
jd_file = st.file_uploader("Job Description", type=["pdf"], key="jd", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

# --- Match & Insights ---
if resume_file and jd_file:
    score, matched, missing, edu_match = calculate_match(resume_file, jd_file)

    st.divider()
    st.markdown(f"### 📊 Match Score: **{score}%**")
    st.progress(score)

    if score >= 85:
        st.success("✅ Excellent Fit! 🎯")
    elif score >= 60:
        st.warning("⚠️ Moderate Fit — Some Skills Missing.")
    else:
        st.error("❌ Low Match — Resume Needs Optimization.")

    st.markdown("### ✅ Matched Skills")
    st.markdown(f"`{', '.join(matched) if matched else 'None'}`")

    st.markdown("### ❌ Missing Skills")
    st.markdown(f"`{', '.join(missing) if missing else 'None'}`")

    st.markdown("### 🎓 Education Match")
    st.markdown("✅ Degree matched" if edu_match else "❌ No matching degree found")
    # AI Suggestions Section
# AI Suggestions Section
st.markdown("### ✨ AI-Powered Resume Improvement Suggestions")

with st.expander("💡 Click to View Suggestions"):
    with st.spinner("Generating smart suggestions..."):
        try:
            tips = suggest_resume_improvements(missing)
            st.markdown(f"<div style='font-size:16px; line-height:1.6;'>{tips}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"⚠️ AI suggestion failed: {e}")
