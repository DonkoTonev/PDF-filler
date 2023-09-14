import PyPDF2
import json
from reportlab.pdfgen import canvas

# Define the file paths for the input PDF and JSON data
pdf_file_path = "empty.pdf"
json_file_path = "example.json"

# Define the watermark text
watermark_text = "DRAFT"  # Change this to your desired watermark text

# Open the JSON file for reading
with open(json_file_path, 'r') as json_file:
    # Load the JSON data into a Python dictionary
    data = json.load(json_file)

# Use PyPDF2 to open the PDF file
pdf = PyPDF2.PdfReader(pdf_file_path)

fields = pdf.get_fields()

# Check if the PDF is encrypted
if pdf.is_encrypted:
    print("PDF is encrypted")
else:
    # Create a PDF writer object to create a new PDF with filled form fields
    pdf_writer = PyPDF2.PdfWriter()

    # Create a PDF canvas for the watermark
    c = canvas.Canvas("watermark.pdf")
    c.setFont("Helvetica", 48)
    c.setFillGray(0.7)
    c.drawString(200, 10, watermark_text)
    c.save()

    watermark_pdf = PyPDF2.PdfReader("watermark.pdf")

    # Iterate through each page in the input PDF
    for page_num in range(len(pdf.pages)):
        # Get the current page
        page = pdf.pages[page_num]

        # Merge the watermark with the original page
        page.merge_page(watermark_pdf.pages[0])

        # Iterate through the fields and values in the JSON data and update the form fields
        for field_name, field_value in data.items():
            pdf_writer.update_page_form_field_values(page, {field_name: field_value})

        # Add the updated page to the PDF writer
        pdf_writer.add_page(page)

    # Specify the output PDF file path
    output_pdf_path = "C:\\Users\\admin\OneDrive\\Desktop\\PDF delivery\\filled_with_watermark.pdf"

    # Open the output PDF file for writing in binary mode
    with open(output_pdf_path, 'wb') as output_pdf_file:
        # Write the PDF content to the output file
        pdf_writer.write(output_pdf_file)

    # Print a success message with the path to the filled PDF with watermark
    print(f"PDF with watermark was successfully created at {output_pdf_path}")
