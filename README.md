# 🧠 AI Resume Analyzer

**AI Resume Analyzer** is a web application that evaluates resumes against job descriptions to generate an **ATS-style compatibility score**, highlight missing skills, and provide actionable improvement suggestions.
Built with **Python (Flask/FastAPI)**, **NLP**, and an interactive **React/Streamlit frontend**, it helps job seekers optimize resumes and recruiters screen candidates faster.

---

## 🚀 Key Features

* 📤 **Resume Upload** – Accept PDF or DOCX files; automatic text extraction.
* 🧾 **Job Description Input** – Paste JD or upload a text file.
* 🧠 **AI-Powered Analysis** – Uses TF-IDF, spaCy, or Transformer embeddings to compute resume-JD similarity.
* 📊 **ATS Match Score** – Shows percentage match between resume and job description.
* 🧩 **Missing Keywords & Skills** – Highlights skills that can improve your match.
* 💡 **Actionable Feedback** – Provides brief, practical suggestions.
* 📈 **Interactive Dashboard** – Visualizes skill overlap and match distribution.

---

## 🧰 Tech Stack

| Layer               | Technologies                                                         |
| ------------------- | -------------------------------------------------------------------- |
| **Frontend**        | React / Streamlit, HTML5, CSS3                                       |
| **Backend**         | Flask / FastAPI                                                      |
| **ML / NLP**        | Python, spaCy, scikit-learn, NLTK, TF-IDF, Hugging Face Transformers |
| **Data Handling**   | pdfplumber, docx2txt, pandas                                         |
| **Deployment**      | Render, Streamlit Cloud, Hugging Face Spaces                         |
| **Version Control** | Git, GitHub                                                          |

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
│
├── backend/
│   ├── app.py           # Flask/FastAPI API
│   ├── model.py         # NLP similarity & keyword extraction
│   ├── utils.py         # Helper functions
│   ├── requirements.txt
│   └── uploads/         # Temporary uploaded resumes
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ResumeUpload.js
│   │   │   ├── JobDescInput.js
│   │   │   └── ResultsCard.js
│   │   └── App.js
│   └── package.json
│
├── notebooks/
│   └── prototype.ipynb  # Early experimentation
│
├── static/              # Screenshots for README
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup & Installation

Follow these steps to run **AI Resume Analyzer** on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DishaChakraborty-11/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

---

### 2️⃣ Backend Setup (Flask/FastAPI)

1. Create a Python virtual environment:

```bash
cd backend
python -m venv venv
```

2. Activate the virtual environment:

* **Windows**:

```bash
venv\Scripts\activate
```

* **Mac/Linux**:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Set environment variables:
   If your backend requires API keys or configs, create a `.env` file in `backend/`:

```text
API_KEY=your_api_key_here
OTHER_CONFIG=value
```

5. Run the backend server:

```bash
python app.py
```

The API will start at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 3️⃣ Frontend Setup (React)

1. Navigate to the frontend folder:

```bash
cd ../frontend
```

2. Install frontend dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm start
```

The frontend will run at: [http://localhost:3000](http://localhost:3000)

> ⚠️ Make sure the backend is running before using the frontend.

---

## 🖼️ Example Usage

**Upload Resume & Job Description**
![Upload Page](static/upload_page.png)

**Results Dashboard**
![Results Dashboard](static/results_dashboard.png)

* The dashboard shows:

  * **ATS Match Score**
  * **Detected vs Missing Skills**
  * **Improvement Suggestions**

---

## 🧮 How It Works

1. **Text Extraction** – Extracts text from uploaded resume and job description.
2. **Preprocessing** – Clean, tokenize, and lemmatize text using spaCy.
3. **Vectorization** – Converts text to vectors using TF-IDF or sentence embeddings.
4. **Similarity Scoring** – Computes cosine similarity between resume & JD.
5. **Skill Extraction** – Identifies missing or extra skills using keyword matching / NER.
6. **Visualization** – Displays results in a clean, interactive dashboard.

### Example Output

| Metric           | Example Value                        |
| ---------------- | ------------------------------------ |
| ATS Match Score  | 82%                                  |
| Missing Keywords | Python, Flask, TensorFlow            |
| Key Strengths    | NLP, Model Deployment, Data Analysis |

---

## 💡 Future Enhancements

* Integrate **LLMs (Gemini/OpenAI)** for richer feedback.
* Add **profile recommendations** (best-fit roles).
* Store **analysis history** in MongoDB.
* Deploy full-stack to **Render / GCP** for live use.

---

## 👩‍💻 Author

**Disha Chakraborty**
B.Tech CSE (AI & ML) | Kolkata, India
🌐 [GitHub](https://github.com/DishaChakraborty-11) | [LinkedIn](https://www.linkedin.com/in/dishachakraborty)

---

## 🪪 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
