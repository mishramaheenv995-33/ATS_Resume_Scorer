"""
ATS Resume Checker - Main Application
An improved resume scoring system with accurate analysis and clean output
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

def check_dependencies():
    """Check if required dependencies are installed"""
    missing_deps = []
    
    try:
        import pdfplumber
    except ImportError:
        missing_deps.append("pdfplumber")
    
    try:
        import pdf2image
    except ImportError:
        missing_deps.append("pdf2image")
    
    try:
        import pytesseract
    except ImportError:
        missing_deps.append("pytesseract")
    
    try:
        from docx import Document
    except ImportError:
        missing_deps.append("python-docx")
    
    try:
        from PIL import Image
    except ImportError:
        missing_deps.append("Pillow")
    
    if missing_deps:
        error_msg = f"""
Missing Dependencies:
{chr(10).join(f'• {dep}' for dep in missing_deps)}

Please install them using:
pip install {' '.join(missing_deps)}

Note: For OCR functionality, you also need:
- Tesseract OCR (https://github.com/tesseract-ocr/tesseract)
- Poppler (for pdf2image)
"""
        messagebox.showerror("Missing Dependencies", error_msg)
        return False
    
    return True

def main():
    """Main application entry point"""
     
    root = tk.Tk()
    root.withdraw()
    
    
    if not check_dependencies():
        return
    
     
    root.deiconify()
    
     
    try:
        from gui import ResumeCheckerApp
        app = ResumeCheckerApp(root)
        
         
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")
        
         
        root.mainloop()
        
    except ImportError as e:
        messagebox.showerror("Import Error", f"Failed to import application modules: {e}")
    except Exception as e:
        messagebox.showerror("Application Error", f"Failed to start application: {e}")

if __name__ == "__main__":
    main()
