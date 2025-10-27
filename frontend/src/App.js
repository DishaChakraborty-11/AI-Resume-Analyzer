import React, { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import JobDescInput from "./components/JobDescInput";
import ResultsCard from "./components/ResultsCard";
import "./App.css";

function App() {
  const [results, setResults] = useState(null);

  return (
    <div className="app-container">
      <h1 className="title">🧠 AI Resume Analyzer</h1>
      <div className="input-section">
        <ResumeUpload setResults={setResults} />
        <JobDescInput setResults={setResults} />
      </div>
      {results && <ResultsCard results={results} />}
    </div>
  );
}

export default App;
