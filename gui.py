import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import traceback

from extractors import extract_text_resume
from checker import ResumeChecker

class ResumeCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATS Resume Checker")
        self.root.geometry("900x700")
        
        self.checker = None
        self.resume_text = ""
        
         
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
         
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
         
        title_label = ttk.Label(main_frame, text="ATS Resume Checker", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=(0, 10))
        
         
        instruction_frame = ttk.Frame(main_frame)
        instruction_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        instruction_frame.columnconfigure(0, weight=1)
        
        ttk.Label(instruction_frame, text="Select a resume file (PDF or Word):").grid(row=0, column=0, sticky=tk.W)
        ttk.Button(instruction_frame, text="Browse Resume", 
                  command=self.browse_file).grid(row=0, column=1, padx=(10, 0))
        
         
        results_frame = ttk.Frame(main_frame)
        results_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
         
        self.text_output = tk.Text(results_frame, height=30, width=100, 
                                  wrap=tk.WORD, font=('Consolas', 10))
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, 
                                 command=self.text_output.yview)
        self.text_output.configure(yscrollcommand=scrollbar.set)
        
        self.text_output.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    def browse_file(self):
        """Browse and process resume file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Resume Files", "*.pdf *.doc *.docx")],
            title="Select Resume File"
        )
        
        if file_path:
            self.text_output.delete('1.0', tk.END)
            self.text_output.insert(tk.END, f"Processing resume: {file_path}\n")
            self.text_output.insert(tk.END, "=" * 80 + "\n\n")
            self.root.update()
            
            try:
                 
                self.resume_text = extract_text_resume(file_path)
                
                if not self.resume_text.strip():
                    messagebox.showwarning("Warning", 
                        "Could not extract text from this file. Please check if the file is readable.")
                    return
                
                 
                self.checker = ResumeChecker(self.resume_text)
                percentage, scores, details = self.checker.calculate_score()
                
                 
                self.display_results(percentage, scores, details)
                
            except Exception as e:
                error_msg = f"Error processing resume: {str(e)}"
                messagebox.showerror("Error", error_msg)
                print(f"Error: {e}\n{traceback.format_exc()}")

    def display_results(self, percentage, scores, details):
        """Display results in a clean format"""
         
        self.text_output.insert(tk.END, f"📊 OVERALL RESUME SCORE: {percentage:.1f}%\n")
        self.text_output.insert(tk.END, f"📈 RATING: {details['Overall Rating']}\n")
        self.text_output.insert(tk.END, "=" * 80 + "\n\n")
        
         
        self.text_output.insert(tk.END, "📋 DETAILED SECTION SCORES:\n")
        self.text_output.insert(tk.END, "-" * 40 + "\n")
        
        for section, score in scores.items():
            if section == 'Contact Details':
                max_score = 4
            elif section in ['Structure', 'Work Experience', 'Skills']:
                max_score = 5
            elif section == 'Education':
                max_score = 4
            elif section == 'Projects':
                max_score = 3
            elif section == 'Achievements':
                max_score = 2
            else:   
                max_score = 5
            
            percentage_score = (score / max_score) * 100 if max_score > 0 else 0
            self.text_output.insert(tk.END, f"{section:.<20} {score:.1f}/{max_score} ({percentage_score:.1f}%)\n")
        
        self.text_output.insert(tk.END, "\n")
        
         
        self.text_output.insert(tk.END, "🔍 DETAILED FINDINGS:\n")
        self.text_output.insert(tk.END, "=" * 40 + "\n\n")
        
        for section, items in details.items():
            if section == 'Overall Rating':
                continue
                
            self.text_output.insert(tk.END, f"📌 {section.upper()}:\n")
            
            if isinstance(items, list) and items:
                for item in items:
                    self.text_output.insert(tk.END, f"   ✓ {item}\n")
            elif isinstance(items, list) and not items:
                self.text_output.insert(tk.END, "   ❌ No items found\n")
            else:
                self.text_output.insert(tk.END, f"   {items}\n")
            
            self.text_output.insert(tk.END, "\n")
        
         
        self.show_recommendations(percentage, scores, details)

    def show_recommendations(self, percentage, scores, details):
        """Show improvement recommendations"""
        self.text_output.insert(tk.END, "💡 RECOMMENDATIONS FOR IMPROVEMENT:\n")
        self.text_output.insert(tk.END, "=" * 45 + "\n")
        
        recommendations = []
        
        if scores.get('Contact Details', 0) < 3:
            recommendations.append("• Add missing contact information (phone, email, location, LinkedIn profile)")
        
        if scores.get('Work Experience', 0) < 4:
            recommendations.append("• Strengthen work experience section with specific job titles, companies, and dates")
            recommendations.append("• Use action verbs to describe your accomplishments")
        
        if scores.get('Skills', 0) < 3:
            recommendations.append("• Add more relevant technical and soft skills")
            recommendations.append("• Include industry-specific skills and tools")
        
        if scores.get('Education', 0) < 2:
            recommendations.append("• Add educational background with degree, institution, and graduation year")
            recommendations.append("• Consider adding GPA if it's strong (>3.5)")
        
        if scores.get('Projects', 0) < 2:
            recommendations.append("• Include relevant projects with descriptions and technologies used")
            recommendations.append("• Add links to GitHub or portfolio if available")
        
        if scores.get('Achievements', 0) < 1:
            recommendations.append("• Add awards, certifications, or notable achievements")
        
        if not recommendations:
            recommendations.append("• Your resume looks good! Consider minor formatting improvements.")
        
        for rec in recommendations:
            self.text_output.insert(tk.END, f"{rec}\n")
        
        self.text_output.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.text_output.insert(tk.END, "Resume analysis complete! 🎯\n")
