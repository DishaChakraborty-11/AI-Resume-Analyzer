import React from "react";

const ResultsCard = ({ results }) => {
  const { ATS_Match_Score, Detected_Skills, Missing_Skills, Suggestions } = results;

  return (
    <div className="card results-card">
      <h2>📊 Analysis Results</h2>
      <p><strong>ATS Match Score:</strong> {ATS_Match_Score}</p>
      <p><strong>Detected Skills:</strong> {Detected_Skills.join(", ")}</p>
      <p><strong>Missing Skills:</strong> {Missing_Skills.length > 0 ? Missing_Skills.join(", ") : "None 🎉"}</p>
      <ul>
        {Suggestions.map((s, idx) => (
          <li key={idx}>{s}</li>
        ))}
      </ul>
    </div>
  );
};

export default ResultsCard;
