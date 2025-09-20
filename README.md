#  Chat-Driven Excel File Manipulation System

<h2> Overview</h2>
A backend-focused application built with <b>FastAPI</b> that allows users to:
<ul>
  <li> Upload an Excel file (.xls, .xlsx)</li>
  <li> Perform basic operations on columns (add / combine)</li>
  <li> Download the updated file</li>
</ul>
The system is designed to be modular, reusable, and easily extendable.  
A minimal React example is also provided for frontend interaction.

---

<h2> Tech Stack</h2>

<b>Backend:</b>
<ul>
  <li>Python 3.x</li>
  <li>FastAPI</li>
  <li>Pandas</li>
  <li>Uvicorn</li>
</ul>

<b>Frontend (sample only):</b>
<ul>
  <li>React (Hooks, Fetch API)</li>
</ul>

<b>Other:</b>
<ul>
  <li>OpenPyXL (for .xlsx support)</li>
  <li>Storage: Local file system</li>
</ul>

---

<h2> Setup & Run</h2>

<b>1. Install dependencies</b> pip install -r requirements.txt (for fastapi backtend) & npm i (for react frontend)
<b>2. Start server</b> uvicorn main:app --reload & npm run dev

Server will run at: <b>http://127.0.0.1:8000</b> API Docs available at:
Swagger → <b>/docs</b>

<h2> API Endpoints</h2>

<b> Upload Excel File</b>
<code>POST /file/upload</code>
Returns column names.

<b> Perform Operation</b>
<code>POST /file/operation</code>
Supported operations:

<ul> <li><b>add_column</b>: Create a new column as sum of two existing columns</li> <li><b>combine_two_columns</b>: Combine values of two columns</li> </ul>

<b> Download Updated File</b>
<code>GET /file/download</code>
Returns updated Excel file.

<h2> Error Handling</h2>
  Uploading non-Excel file → <b>400 Invalid file format</b>
  Performing operation before upload → <b>400 No file uploaded</b>
  Wrong params → <b>400 Bad Request</b>
  Unexpected issues → <b>500 Internal Server Error</b>
