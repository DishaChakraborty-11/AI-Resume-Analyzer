from flask import Flask, request, jsonify
from model import analyze_resume
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "AI Resume Analyzer Backend is running 🚀"})

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files.get('resume')
    job_desc = request.form.get('job_description')

    if not resume or not job_desc:
        return jsonify({"error": "Please upload resume and job description"}), 400

    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
    resume.save(resume_path)

    results = analyze_resume(resume_path, job_desc)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
