🧠 AI Resume Analyzer and Job Matcher

A smart web application that analyzes resumes to extract key skills using Natural Language Processing (NLP) and matches them with suitable job roles. Built using Flask, Python, and HTML/CSS, this project showcases intelligent resume evaluation and user-friendly design — ideal for students, job seekers, and recruiters.
🔍 Features
    ✅ Upload and parse PDF resumes
    🧠 Extract relevant skills using NLP techniques
    📊 Match extracted skills with predefined job roles
    📈 Assign resume score based on skill matching
    ❌ Show missing skills for targeted roles
    🌐 Interactive and responsive web interface
    📥 Option to export results as PDF (optional)
📁 Project Structure

AI-Resume-Analyzer/
│
├── app.py                # Main Flask backend
├── skills.py             # Skills extraction and job matching logic
├── templates/            # HTML templates (upload.html, result.html)
│   ├── upload.html
│   └── result.html
├── static/               # CSS & images (if any)
├── resumes/              # Uploaded PDF resumes
└── README.md             # Project documentation

 Technologies Used

Python 3.x
Flask
PyMuPDF (fitz) for PDF parsing
HTML, CSS (custom UI styling)
(Optional) pdfkit & wkhtmltopdf for exporting results as PDF

