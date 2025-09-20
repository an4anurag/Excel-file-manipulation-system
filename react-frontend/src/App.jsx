import React, { useState } from "react";
import './App.css'
import config from './config'

const App = () => {
  const [file, setFile] = useState(null);
  const [columns, setColumns] = useState([]);
  const [preview, setPreview] = useState([]);

  // Upload Excel file
  const handleUpload = async () => {
    if (!file) return alert("Please select a file!");

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`/api${config.upload}`, {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setColumns(data.columns);
  };

  // Perform operation
  const handleOperation = async () => {
    const res = await fetch(`/api${config.operation}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        operation: "add_column",
        params: {
          new_column_name: "Total",
          columns_to_sum: ["Price", "Tax"],
        },
      }),
    });

    const data = await res.json();
    setColumns(data.columns);
    setPreview(data.preview);
  };

  // Download file
  const handleDownload = async () => {
    const res = await fetch(`/api${config.download}`);
    const blob = await res.blob();
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = "updated.xlsx";
    link.click();
  };

  return (
    <>
      <h2>Upload Excel File</h2>
      <input
        type="file"
        accept=".xls,.xlsx"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload</button>

      {columns.length > 0 && (
        <div>
          <h4 style={{margin:'0', padding:'8px'}}>Columns:</h4>
          <ul style={{backgroundColor:'gray'}}>
            {columns.map((col) => (
              <li key={col}>{col}</li>
            ))}
          </ul>
          <button onClick={handleOperation}>Add Total Column</button>
        </div>
      )}

      {preview.length > 0 && (
        <div>
          <h3>Preview:</h3>
          <pre style={{backgroundColor:'gray'}}>{JSON.stringify(preview, null, 2)}</pre>
          <button onClick={handleDownload}>Download Updated File</button>
        </div>
      )}
    </>
  );
}
export default App;