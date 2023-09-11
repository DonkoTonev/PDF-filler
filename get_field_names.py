# import PyPDF2

# def get_pdf_field_names(pdf_path):
#     field_names = []

#     # Open the PDF file in read-binary mode
#     with open(pdf_path, 'rb') as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Loop through each page of the PDF
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             annotations = page['/Annots']

#             # Check if the page has annotations (form fields)
#             if annotations:
#                 for annotation in annotations:
#                     annotation_obj = annotation.get_object()
#                     if '/T' in annotation_obj:
#                         field_name = annotation_obj['/T']
#                         field_names.append(field_name)

#     return field_names

# # Specify the path to your PDF file
# pdf_path = "notice.pdf"

# # Get the field names from the PDF
# field_names = get_pdf_field_names(pdf_path)

# # Print the field names
# for field_name in field_names:
#     print(field_name)





import PyPDF2

def get_pdf_field_names(pdf_path):
    field_names = []

    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Loop through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]

            # Check if the page has annotations (form fields)
            if '/Annots' in page:
                annotations = page['/Annots']
                for annotation in annotations:
                    annotation_obj = annotation.get_object()
                    if '/T' in annotation_obj:
                        field_name = annotation_obj['/T']
                        field_names.append(field_name)

    return field_names

# Specify the path to your PDF file
pdf_path = "notice.pdf"

# Get the field names from the PDF
field_names = get_pdf_field_names(pdf_path)

# Print the field names
for field_name in field_names:
    print(field_name)
