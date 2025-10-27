# 🧠 AI Resume Analyzer

An AI-powered web application that evaluates resumes against job descriptions to generate an **ATS-style compatibility score**, highlight missing skills, and suggest improvements.  
Built using **Python (Flask/FastAPI)**, **NLP**, and an interactive **React/Streamlit frontend**.

---

## 🚀 Features

- 📤 **Resume Upload** – Accepts PDF or DOCX files and extracts text automatically.  
- 🧾 **Job Description Input** – Paste a JD or upload a text file.  
- 🧠 **NLP-Based Analysis** – Uses TF-IDF / spaCy / Transformer embeddings to compare keywords and compute similarity score.  
- 📊 **ATS Match Score** – Displays how well the resume fits the JD.  
- 🧩 **Missing Keywords & Skills** – Highlights skills that can improve the match.  
- 💡 **Improvement Suggestions** – Generates brief, actionable feedback.  
- 📈 **Interactive Dashboard** – Visualizes skill overlap and match distribution.

---

## 🧰 Tech Stack

| Layer | Technologies |
|--------|---------------|
| **Frontend** | React / Streamlit, HTML5, CSS3 |
| **Backend** | Flask / FastAPI |
| **ML / NLP** | Python, spaCy, scikit-learn, NLTK, TF-IDF, Hugging Face Transformers |
| **Data Handling** | pdfplumber, docx2txt, pandas |
| **Deployment** | Render / Streamlit Cloud / Hugging Face Spaces |
| **Version Control** | Git, GitHub |

---

## 📁 Folder Structure

AI-Resume-Analyzer/
│
├── backend/
│ ├── app.py # Flask/FastAPI API
│ ├── model.py # NLP similarity & keyword extraction
│ ├── utils.py # Helper functions
│ ├── requirements.txt
│ └── uploads/ # Temporary uploaded resumes
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── ResumeUpload.js
│ │ │ ├── JobDescInput.js
│ │ │ ├── ResultsCard.js
│ │ └── App.js
│ └── package.json
│
├── notebooks/
│ └── prototype.ipynb # Early experimentation
│
├── static/ # (optional) screenshots for README
├── .gitignore
└── README.md


---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/DishaChakraborty-11/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

2️⃣ Backend Setup

cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

3️⃣ Frontend Setup (if React)

cd ../frontend
npm install
npm start

The app will start locally at: http://localhost:3000
 (React) or 
 http://127.0.0.1:5000
 (Flask). 

 ---

## 🎨 UI/UX Design

The user interface for **AI Resume Analyzer** was designed in **Figma**, following a clean, modern, and responsive layout inspired by ATS dashboards.

### 🖼️ Design Previews

#### Upload Page
![Upload Page](static/upload_page.png)

#### Results Dashboard
![Results Dashboard](static/results_dashboard.png)

### 📄 Complete Design File
- [📘 View Live Figma Design](https://www.figma.com/make/rsI30ILzJSu0YTIm8aBANC/AI-Resume-Analyzer-Interface?node-id=0-1&p=f&t=YP6hAkcbT3gDRPar-0&fullscreen=1)  
- [📄 Download PDF (UI Design)](static/AI_Resume_Analyzer_UI_Design.pdf)

**Highlights:**
- Simple upload interface with job description input  
- Dashboard showing ATS Match Score, Detected & Missing Skills  
- Pastel theme: light blue (#3b49df) accents with white cards  
- Responsive layout optimized for web and mobile  

---


🧮 How It Works

Text Extraction: Extract text from uploaded resume and job description.

Preprocessing: Clean, tokenize, and lemmatize using spaCy.

Vectorization: Convert text into vectors via TF-IDF or sentence embeddings.

Similarity Scoring: Compute cosine similarity between resume & JD.

Skill Extraction: Identify missing or extra skills using keyword matching or NER.

Visualization: Render results on the frontend dashboard.

📊 Example Output
Metric	Example Value
ATS Match Score	82%
Missing Keywords	Python, Flask, TensorFlow
Key Strengths	NLP, Model Deployment, Data Analysis

(This table updates dynamically once you upload a resume.)

💡 Future Enhancements

Integrate LLM (Gemini/OpenAI) for richer feedback.

Add profile recommendations (e.g., best-fit roles).

Store analysis history with MongoDB.

Deploy full stack to Render or GCP for live use.

👩‍💻 Author

Disha Chakraborty
B.Tech CSE (AI & ML) | Kolkata, India
🌐 GitHub | LinkedIn

🪪 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

