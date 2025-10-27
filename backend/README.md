# 🧠 AI Resume Analyzer – Backend

This is the **Flask-based backend API** for the AI Resume Analyzer web application.  
It processes uploaded resumes, compares them with job descriptions using **NLP and TF-IDF similarity**, and returns an **ATS-style compatibility score**, detected skills, and improvement suggestions.

![Python](https://img.shields.io/badge/Language-Python-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## ⚙️ Tech Stack
- **Backend Framework:** Flask  
- **Libraries:** scikit-learn, spaCy, pdfplumber, docx2txt  
- **Modeling:** TF-IDF Vectorization + Cosine Similarity  
- **Language:** Python 3.10+  

---

## 🚀 Quick Start

### 1️⃣ Create and activate a virtual environment
'''bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask server
python app.py


By default, the API runs at:
👉 http://127.0.0.1:5000

🧩 API Endpoint
POST /analyze

Analyzes the uploaded resume against a job description.

🧾 Request

Form-Data:

resume → File (.pdf or .docx)

job_description → Text (string)

📤 Response
{
  "ATS_Match_Score": "82.5%",
  "Detected_Skills": ["python", "flask", "machine learning"],
  "Missing_Skills": ["tensorflow", "docker"],
  "Suggestions": ["Add skills like tensorflow, docker to improve your score."]
}

📁 Folder Structure
backend/
│
├── app.py               # Main Flask API
├── model.py             # NLP and similarity logic
├── utils.py             # Helper functions
├── requirements.txt     # Dependencies
└── uploads/             # Temporary resume storage

🧠 How It Works

> Extracts text from uploaded PDF/DOCX using pdfplumber or docx2txt.

> Cleans and preprocesses text with spaCy.

> Converts resume & JD into TF-IDF vectors.

> Calculates cosine similarity to generate ATS score.

> Extracts detected and missing skills from both texts.

🧪 Testing with cURL
curl -X POST -F "resume=@sample_resume.pdf" \
     -F "job_description=Looking for a Python Flask developer" \
     http://127.0.0.1:5000/analyze
