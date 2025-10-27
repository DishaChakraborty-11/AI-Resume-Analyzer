from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber
import docx2txt
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)  # allow frontend requests

nlp = spacy.load("en_core_web_sm")

# ---------- Helper Functions ---------- #

def extract_text_from_resume(file):
    """Extract text from PDF or DOCX resumes."""
    text = ""
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file.filename.endswith(".docx"):
        text = docx2txt.process(file)
    else:
        text = file.read().decode(errors="ignore")
    return text


def clean_text(text):
    """Clean punctuation, numbers, and stopwords."""
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)


def calculate_similarity(resume_text, jd_text):
    """Calculate ATS match score using TF-IDF + Cosine Similarity."""
    corpus = [resume_text, jd_text]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
    return round(score, 2)


def extract_skills(text):
    """Simple keyword-based skill detection (expandable)."""
    skills = [
        "python", "machine learning", "deep learning", "flask", "react",
        "django", "sql", "data analysis", "tensorflow", "pandas", "numpy",
        "html", "css", "javascript", "nlp", "excel"
    ]
    found = [skill for skill in skills if skill.lower() in text.lower()]
    return list(set(found))


# ---------- API Endpoint ---------- #

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files or "job_description" not in request.form:
        return jsonify({"error": "Missing required fields"}), 400

    resume = request.files["resume"]
    jd_text = request.form["job_description"]

    resume_text = extract_text_from_resume(resume)
    if not resume_text.strip():
        return jsonify({"error": "Resume text could not be extracted properly"}), 400

    # Clean text and compute similarity
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    score = calculate_similarity(resume_clean, jd_clean)

    # Skill analysis
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    missing_skills = [s for s in jd_skills if s not in resume_skills]

    suggestions = (
        f"Add skills like {', '.join(missing_skills)} to improve your match score."
        if missing_skills
        else "Your resume covers most required skills!"
    )

    return jsonify({
        "ATS_Match_Score": f"{score}%",
        "Detected_Skills": resume_skills,
        "Missing_Skills": missing_skills,
        "Suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(debug=True)
