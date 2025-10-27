import React, { useState } from "react";
import axios from "axios";

const ResumeUpload = ({ setResults }) => {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !jobDesc) {
      alert("Please upload a resume and paste a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_description", jobDesc);

    try {
      const res = await axios.post("http://127.0.0.1:5000/analyze", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResults(res.data);
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong. Check the backend connection!");
    }
  };

  return (
    <div className="card">
      <h2>📤 Upload Resume</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".pdf, .docx"
          onChange={(e) => setFile(e.target.files[0])}
          required
        />
        <textarea
          placeholder="Paste Job Description here..."
          rows={6}
          onChange={(e) => setJobDesc(e.target.value)}
          required
        ></textarea>
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
};

export default ResumeUpload;
