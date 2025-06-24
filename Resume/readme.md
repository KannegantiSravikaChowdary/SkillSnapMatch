# 🎯 Smart Resume Match

A student-centric AI/ML-powered resume matcher that compares your resume with job descriptions and gives:

- 🔍 Detected Job Role
- 🎯 Match Score
- 🛠️ Missing Skills
- 📚 Learning Recommendations
- 🎓 Education Validation

## 🚀 Features
- Role detection based on JD keywords.
- Skill match analysis with recommendations.
- Education check for field-relevance.
- Built with Streamlit UI, Python, and NLP logic.

## 📁 Project Structure
smart_resume_match/
├── app.py # Streamlit frontend
├── matcher.py # Core resume-JD matching logic
├── recommender.py # Skill-based learning recommendation
├── role_detector.py # JD role classification
├── utils/
│ ├── init.py
| |── education_validator.py
│── data/
│   ├── sample_resume&JD/
│   │   ├── Resume1.pdf
│       |── Resume2.pdf
│       |- sample_job_description
│
├── requirements.txt
└── README.md └── education_validator.py


## 🔧 Installation
## ⚙️ Setup Instructions

1. **Clone or Download** this repo

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt  

3. **Run the app (choose one)**:

    # If streamlit is available globally
    streamlit run app.py

    # If not, use full path (Windows)
    & "$env:USERPROFILE\AppData\Roaming\Python\Python313\Scripts\streamlit.exe" run app.py

    # Or use module
    python -m streamlit run app.py


## 🔒 Security
    Your resume and job description are processed locally
    OpenAI API key is stored securely via .env
    No data is saved or transmitted externally
