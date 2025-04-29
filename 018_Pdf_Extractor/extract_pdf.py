import os
import sys
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

def extract_text_from_pdf(pdf_path, output_path=None):
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: File '{pdf_path}' not found.")
            return False
            
        reader = PdfReader(pdf_path)
        
        num_pages = len(reader.pages)
        print(f"Found {num_pages} pages in the PDF.")
        
        all_text = ""
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            all_text += page.extract_text() + "\n\n"
            
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(all_text)
            print(f"Text extracted and saved to '{output_path}'")
        else:
            print("\n--- EXTRACTED TEXT ---\n")
            print(all_text)
            
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    pdf_file = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    
    if not pdf_file:
        print("No file selected. Exiting.")
        sys.exit()
    
    save_output = input("Save output to a text file? (y/n): ").lower().strip()
    
    output_file = None
    if save_output == 'y':
        output_file = filedialog.asksaveasfilename(
            title="Save extracted text as",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
    
    extract_text_from_pdf(pdf_file, output_file)