"""
with open("baseball.jpg", 'rb') as file:
	data = file.read()

with open("baseball-copy.jpg", 'wb') as file:
	file.write(data)
	
with open("baseball-part.jpg", 'wb') as file:
	file.write(data)
	
with open("sample.mp3", 'rb') as file:
    contents = file.read()

with open("sample-twice.mp3", 'wb') as file:
    file.write(contents)
    file.write(contents)

with open("baseball.jpg", 'rb') as file:
    data = file.read()

with open("baseball-part.jpg", 'wb') as file:
    file.write(data[:300000000])
"""
################### reading pdf and extract text from the pdf###########################################################
"""
import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Example usage
resume_path = 'resume.pdf'
resume_text = read_pdf(resume_path)
print(resume_text)

pdf_text = read_pdf('resume.pdf')
 
 """
################### reading pdf  and extract text from the pdf spesfic page number 3 ###################################
"""
import PyPDF2


def read_pdf(file_path, pages=None):
   
    Reads text from specific pages of a PDF file.

    :param file_path: Path to the PDF file.
    :param pages: List of page numbers to extract text from (1-indexed). If None, extracts all pages.
    :return: Extracted text from specified pages.
   
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        total_pages = len(reader.pages)
        
        if pages is None:
            pages = range(1, total_pages + 1)
        
        for page_num in pages:
            if 1 <= page_num <= total_pages:
                page = reader.pages[page_num - 1]  # Convert to 0-indexed
                text += page.extract_text()
            else:
                print(f"Page number {page_num} is out of range (1-{total_pages}).")
        return text


# Example usage
resume_path = 'resume.pdf'
specific_pages = [3]  # Specify the pages you want to extract text from (only page 3)
resume_text_page3 = read_pdf(resume_path, specific_pages)
print(resume_text_page3)
"""


#######################################################################################################################
"""
1.9.3. BONUS Writing a reproduced PDF

3. Create a new PDF file that contains only the first page.
"""

"""
import PyPDF2
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch


def read_pdf(file_path, pages=None):
   
    Reads text from specific pages of a PDF file.

    :param file_path: Path to the PDF file.
    :param pages: List of page numbers to extract text from (1-indexed). If None, extracts all pages.
    :return: Extracted text from specified pages.
   
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        total_pages = len(reader.pages)
        if pages is None:
            pages = range(1, total_pages + 1)
        
        for page_num in pages:
            if 1 <= page_num <= total_pages:
                page = reader.pages[page_num - 1]  # Convert to 0-indexed
                text += page.extract_text()
            else:
                print(f"Page number {page_num} is out of range (1-{total_pages}).")
        return text


def write_pdf(output_path, text):
   
    Writes text to a new PDF file with word wrapping to fit within margins on an A4 page.

    :param output_path: Path to the output PDF file.
    :param text: Text to be written to the PDF file.
   
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    style = styles['BodyText']
    
    # Split the text by lines and create Paragraphs
    lines = text.split('\n')
    story = []
    for line in lines:
        story.append(Paragraph(line, style))
        story.append(Spacer(1, 0 * inch))  # Add space between lines
    
    doc.build(story)


# Example usage
resume_path = 'resume.pdf'
specific_pages = [1]  # Specify the pages you want to read from (only page 1)
resume_text = read_pdf(resume_path, specific_pages)
print(resume_text)

# Write the extracted text to a new PDF
output_path = 'reproducedA4.pdf'
write_pdf(output_path, resume_text)
print(f"Text has been written to {output_path}")
"""
"""
4. The last page of the PDF is rotated by accident. Save a new pdf file where the last page is rotated back so it’s
readable again.
"""
"""
import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch


def read_and_rotate_pdf(input_path, output_path, pages=None, rotation=90):
    Reads text from specific pages of a PDF file, rotates those pages, and writes the result to a new PDF file.

    :param input_path: Path to the input PDF file.
    :param output_path: Path to the output PDF file.
    :param pages: List of page numbers to rotate (1-indexed). If None, rotates all pages.
    :param rotation: Degrees to rotate pages (clockwise). Must be one of 90, 180, 270.
    reader = PyPDF2.PdfReader(input_path)
    writer = PyPDF2.PdfWriter()
    total_pages = len(reader.pages)
    
    if pages is None:
        pages = range(1, total_pages + 1)
    
    for page_num in range(1, total_pages + 1):
        page = reader.pages[page_num - 1]
        if page_num in pages:
            page = page.rotate(rotation)
        writer.add_page(page)
    
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    print(f"Rotated PDF saved as {output_path}")


def read_pdf(file_path, pages=None):
    Reads text from specific pages of a PDF file.

    :param file_path: Path to the PDF file.
    :param pages: List of page numbers to extract text from (1-indexed). If None, extracts all pages.
    :return: Extracted text from specified pages.
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        total_pages = len(reader.pages)
        
        if pages is None:
            pages = range(1, total_pages + 1)
        
        for page_num in pages:
            if 1 <= page_num <= total_pages:
                page = reader.pages[page_num - 1]  # Convert to 0-indexed
                text += page.extract_text()
            else:
                print(f"Page number {page_num} is out of range (1-{total_pages}).")
        return text


def write_pdf(output_path, text):
    Writes text to a new PDF file with word wrapping to fit within margins on an A4 page.

    :param output_path: Path to the output PDF file.
    :param text: Text to be written to the PDF file.
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    style = styles['BodyText']
    
    # Split the text by lines and create Paragraphs
    lines = text.split('\n')
    story = []
    for line in lines:
        story.append(Paragraph(line, style))
        story.append(Spacer(1, 0.2 * inch))  # Add space between lines
    
    doc.build(story)


# Example usage
resume_path = 'resume.pdf'
specific_pages = [4]  # Specify the pages you want to read from (only page 1)
resume_text = read_pdf(resume_path, specific_pages)
print(resume_text)

# Write the extracted text to a new PDF
output_text_path = 'reproduced4_rotated_90.pdf'
write_pdf(output_text_path, resume_text)
print(f"Text has been written to {output_text_path}")

# Rotate the first page of the original PDF and save it as a new file
output_rotated_path = 'rotated_90.pdf'
read_and_rotate_pdf(resume_path, output_rotated_path, pages=[4], rotation=90)


#######################################################################################################################

5. Reproduce a new PDF with a watermark applied to all of the pages. Use this watermark PDF. The final output should
 look like this:
#######################################################################################################################
"""
import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_watermark(watermark_path, text):
    """
    Creates a PDF file with the watermark text.

    :param watermark_path: Path to the watermark PDF file.
    :param text: Watermark text.
    """
    c = canvas.Canvas(watermark_path, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 40)
    c.saveState()
    c.translate(width / 2, height / 2)
    c.rotate(45)
    c.drawCentredString(0, 0, text)
    c.restoreState()
    c.save()

# Example usage to create a watermark PDF
watermark_text = "CONFIDENTIAL"
watermark_path = 'watermark.pdf'
create_watermark(watermark_path, watermark_text)
print(f"Watermark created at {watermark_path}")
#######################################################################################################################

def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path):
    """
    Adds a watermark to all pages of a PDF file.

    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to the output PDF file with watermarks.
    :param watermark_pdf_path: Path to the watermark PDF file.
    """
    with open(input_pdf_path, 'rb') as input_file, open(watermark_pdf_path, 'rb') as watermark_file:
        input_pdf = PyPDF2.PdfReader(input_file)
        watermark_pdf = PyPDF2.PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        output_pdf = PyPDF2.PdfWriter()

        for i in range(len(input_pdf.pages)):
            page = input_pdf.pages[i]
            page.merge_page(watermark_page)
            output_pdf.add_page(page)

        with open(output_pdf_path, 'wb') as output_file:
            output_pdf.write(output_file)
    print(f"Watermark added to {output_pdf_path}")

# Example usage to add watermark to a PDF
input_pdf_path = 'resume.pdf'
output_pdf_path = 'watermarked_resume.pdf'
add_watermark(input_pdf_path, output_pdf_path, watermark_path)

#######################################################################################################################

def create_watermark(watermark_path, text):
    """
    Creates a PDF file with the watermark text.

    :param watermark_path: Path to the watermark PDF file.
    :param text: Watermark text.
    """
    c = canvas.Canvas(watermark_path, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 40)
    c.saveState()
    c.translate(width / 2, height / 2)
    c.rotate(45)
    c.drawCentredString(0, 0, text)
    c.restoreState()
    c.save()

def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path):
    """
    Adds a watermark to all pages of a PDF file.

    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to the output PDF file with watermarks.
    :param watermark_pdf_path: Path to the watermark PDF file.
    """
    with open(input_pdf_path, 'rb') as input_file, open(watermark_pdf_path, 'rb') as watermark_file:
        input_pdf = PyPDF2.PdfReader(input_file)
        watermark_pdf = PyPDF2.PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        output_pdf = PyPDF2.PdfWriter()

        for i in range(len(input_pdf.pages)):
            page = input_pdf.pages[i]
            page.merge_page(watermark_page)
            output_pdf.add_page(page)

        with open(output_pdf_path, 'wb') as output_file:
            output_pdf.write(output_file)
    print(f"Watermark added to {output_pdf_path}")

# Example usage
watermark_text = "Dr: Asmamaw Yehun"
watermark_path = 'watermark.pdf'
create_watermark(watermark_path, watermark_text)
print(f"Watermark created at {watermark_path}")

input_pdf_path = 'resume.pdf'
output_pdf_path = 'watermarked_resume.pdf'
add_watermark(input_pdf_path, output_pdf_path, watermark_path)

#######################################################################################################################












