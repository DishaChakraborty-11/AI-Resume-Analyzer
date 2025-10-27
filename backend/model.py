import pdfplumber
import docx2txt
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import clean_text, extract_skills

def extract_text_from_file(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload .pdf or .docx.")
    return text

def analyze_resume(resume_path, job_desc):
    resume_text = extract_text_from_file(resume_path)
    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    score = round(similarity * 100, 2)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)
    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "ATS_Match_Score": f"{score}%",
        "Detected_Skills": list(resume_skills),
        "Missing_Skills": missing_skills,
        "Suggestions": [
            f"Add skills like {', '.join(missing_skills[:5])} to improve your score."
        ] if missing_skills else ["Excellent match! Your resume aligns well with the JD."]
    }
