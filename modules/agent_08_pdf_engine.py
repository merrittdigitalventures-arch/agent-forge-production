import json
import os
from fpdf import FPDF

class PDFEngine:
    def __init__(self):
        with open('style_manifest.json', 'r') as f:
            self.manifest = json.load(f)

    def convert_to_pdf(self, source_file, output_name):
        if not os.path.exists(source_file):
            print(f"❌ Source {source_file} missing.")
            return
            
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
        
        # Header Branding
        pdf.cell(200, 10, txt=f"MERRITT DIGITAL: {self.manifest['niche'].upper()}", ln=True, align='C')
        pdf.ln(10)
        
        with open(source_file, 'r') as f:
            for line in f:
                # Basic sanitization for FPDF
                pdf.multi_cell(0, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'))
        
        pdf.output(output_name)
        print(f"📑 [PDF ENGINE] Generated: {output_name}")

if __name__ == "__main__":
    engine = PDFEngine()
    # Convert core assets
    engine.convert_to_pdf('stack_suggestions.md', 'Alpha_Stack_Suggestions.pdf')
    engine.convert_to_pdf('alpha_playbook.md', 'Alpha_Strategy_Playbook.pdf')
