# Import necessary libraries
import PyPDF2
import json

# Define the file paths for the input PDF and JSON data
pdf_file_path = "example.pdf"
json_file_path = "file.json"

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

    # Iterate through each page in the input PDF
    for page_num in range(len(pdf.pages)):
        # Get the current page
        page = pdf.pages[page_num]

        # Iterate through the fields and values in the JSON data
        for field_name, field_value in data.items():
            # Update the form field values on the current page
            pdf_writer.update_page_form_field_values(page, {field_name: field_value})

        # Add the updated page to the PDF writer
        pdf_writer.add_page(page)

    # Specify the output PDF file path
    output_pdf_path = "C:\\Users\\admin\\OneDrive\\Desktop\\sample.pdf"

    # Open the output PDF file for writing in binary mode
    with open(output_pdf_path, 'wb') as output_pdf_file:
        # Write the PDF content to the output file
        pdf_writer.write(output_pdf_file)

    # Print a success message with the path to the filled PDF
    print(f"PDF was successfully filled at {output_pdf_path}")

