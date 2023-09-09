import PyPDF2
import json

# Път до вашия PDF файл
pdf_file_path = "example.pdf"

# Път до вашия JSON файл със стойности за попълване
json_file_path = "file.json"

# Отваряне на JSON файл и зареждане на стойностите в речник
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Отваряне на PDF файла
pdf = PyPDF2.PdfReader(pdf_file_path)

# Проверка за наличие на попълними полета в PDF файла
if pdf.is_encrypted:
    print("PDF файлът е кодиран и не може да бъде попълнен.")
else:
    pdf_writer = PyPDF2.PdfWriter()

    # Обхождане на всички страници на PDF файла
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]

        # Попълване на полетата в текущата страница със стойности от JSON
        for field_name, field_value in data.items():
            pdf_writer.update_page_form_field_values(page, {field_name: field_value})

        pdf_writer.add_page(page)

    # Запис на резултата в нов PDF файл
    output_pdf_path = "C:\\Users\\admin\\OneDrive\\Desktop\\DEMO\\sample.pdf"
    with open(output_pdf_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)

    print(f"PDF файла беше успешно попълнен и записан в {output_pdf_path}")
