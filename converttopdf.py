from fpdf import FPDF
import json

def json_to_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, json.dumps(data, indent=4))

    pdf.output(output_file)

json_to_pdf("output.json", "output.pdf")
