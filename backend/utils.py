import re
import spacy

# Load spaCy English model (run 'python -m spacy download en_core_web_sm' once)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()

def extract_skills(text):
    common_skills = [
        "python", "java", "c++", "machine learning", "deep learning",
        "data analysis", "sql", "flask", "django", "pandas",
        "numpy", "tensorflow", "pytorch", "nlp", "react", "javascript",
        "html", "css", "cloud", "docker", "git"
    ]
    found = set()
    text = text.lower()
    for skill in common_skills:
        if skill in text:
            found.add(skill)
    return found
