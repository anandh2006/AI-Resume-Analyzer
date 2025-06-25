from flask import Flask, render_template, request
import fitz  # PyMuPDF
import os
from skills import extract_skills, match_jobs

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"[ERROR] Failed to open PDF: {e}")
        return "Error: Unable to extract text from this PDF file."
    return text

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return "No file part"

    file = request.files['resume']
    if file.filename == '':
        return "No selected file"

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        print("✅ Resume saved successfully:", filepath)

        extracted_text = extract_text_from_pdf(filepath)
        skills = extract_skills(extracted_text)
        matched_jobs = match_jobs(skills)

        # Debug info
        print("Extracted Skills:", skills)
        print("Matched Jobs:", matched_jobs)

        return render_template('result.html',
                               resume_text=extracted_text,
                               extracted_skills=skills,
                               matched_jobs=matched_jobs)

if __name__ == '__main__':
    app.run(debug=True)
