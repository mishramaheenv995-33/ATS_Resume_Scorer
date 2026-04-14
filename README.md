# 📄 ATS Resume Checker

An intelligent Resume Analysis Tool that evaluates resumes based on ATS (Applicant Tracking System) standards.
This project extracts text from resumes (PDF, DOCX, Images) and provides a detailed score along with improvement suggestions.

---

## 🚀 Features

* 📂 Supports multiple formats: PDF, DOCX, Images
* 🔍 Extracts text using OCR (Tesseract)
* 📊 Generates overall resume score (percentage)
* 📈 Section-wise analysis:

  * Contact Details
  * Work Experience
  * Skills
  * Education
  * Projects
  * Achievements
* 💡 Provides recommendations to improve resume
* 🖥️ Simple and clean GUI using Tkinter

---

## 🛠️ Tech Stack

* Python
* Tkinter (GUI)
* pdfplumber
* pytesseract (OCR)
* pdf2image
* python-docx
* Pillow

---

## 📁 Project Structure

project/
│── main.py          # Entry point
│── gui.py           # GUI application
│── checker.py       # Resume analysis logic
│── extractors.py    # Text extraction (PDF, DOCX, Image)

---

## ⚙️ Requirements

### 🔹 Install Python (3.8 or above)

### 🔹 Install required libraries

Run this command:

pip install pdfplumber pdf2image pytesseract python-docx pillow

OR use requirements file:

pip install -r requirements.txt

---

## 📄 requirements.txt

Create a file named **requirements.txt** and add:

pdfplumber
pdf2image
pytesseract
python-docx
Pillow

---

## ⚠️ Additional Setup (VERY IMPORTANT)

### 1️⃣ Install Tesseract OCR

Download from:
https://github.com/tesseract-ocr/tesseract

After installation, add this path:

C:\Program Files\Tesseract-OCR\tesseract.exe

---

### 2️⃣ Install Poppler (Required for PDF image processing)

Download Poppler for Windows and add its "bin" folder to system PATH.

---

## ▶️ How to Run (Command Prompt)

### Step 1: Open Command Prompt

### Step 2: Switch to your project folder

D:
cd intenship\4_four_task

---

### Step 3: Run the project

python main.py

---

## 📌 How It Works

1. User selects a resume file
2. System extracts text using:

   * pdfplumber (PDF)
   * pytesseract (OCR)
   * python-docx (Word files)
3. Resume is analyzed using scoring algorithm
4. Results displayed in GUI

---

## 📊 Output

* Overall Resume Score (in %)
* Section-wise score breakdown
* Detailed findings
* Suggestions for improvement

---

## 📷 Screenshots

(Add your GUI screenshot here)

---

## 💻 Example Usage

1. Run the application
2. Click "Browse Resume"
3. Select your resume file
4. View score and suggestions

---

## 🎯 Future Improvements

* Convert into web app (Flask/Django)
* Add AI-based resume suggestions
* Add job matching system
* Improve UI design

---

## 👨‍💻 Author

Your Name

---

## ⭐ GitHub Usage

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py

---

## 📢 Note

Make sure Tesseract OCR and Poppler are properly installed, otherwise OCR and PDF features may not work.
