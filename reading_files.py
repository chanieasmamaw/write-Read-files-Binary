

# 1.7.1. Mini exercises----- write/Read files ##########################################################################
"""
1. Create an identical copy of olympic-medals.csv called olympic-medals-copy.csv. Open the new file in File Explorer
or Finder, and make sure it’s identical.
"""

# Copy the contents of olympic-medals.csv to olympic-medals-copy.csv
with open("olympic-medals.csv", 'r') as source_file:
    data = source_file.readlines()

with open("olympic-medals-copy.csv", 'w') as destination_file:
    destination_file.writelines(data)

# Read and print the contents of olympic-medals-copy.csv
with open("olympic-medals-copy.csv", 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.strip())  # .strip() removes any leading/trailing whitespace including newlines
"""
2. Create a file called olympic-medals-short.csv with only the first 10 line of the original file. Open the new file
to check it was created well.
"""
# Copy the first 10 lines of olympic-medals.csv to olympic-medals-copy.csv
with open("olympic-medals.csv", 'r') as source_file:
    data = [next(source_file) for _ in range(10)]

with open("olympic-medals-copy.csv", 'w') as destination_file:
    destination_file.writelines(data)

# Read and print the contents of olympic-medals-copy.csv
with open("olympic-medals-copy.csv", 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.strip())  # .strip() removes any leading/trailing whitespace including newlines
"""
3. Create a file called olympic-medals-n.csv that will contain only countries that begin with the letter “N”.
"""

# Copy the first 10 lines of olympic-medals.csv to olympic-medals-n.csv
with open("olympic-medals.csv", 'r') as source_file:
    data = source_file.readlines()

with open("olympic-medals-n.csv", 'w') as destination_file:
    destination_file.writelines(data)

# Read and print the contents of olympic-medals-n.csv where the team name contains "N"
with open("olympic-medals-n.csv", 'r') as file:
    for line in file:
        # Split each line into components assuming they are separated by whitespace
        components = line.split()
        if components:
            TEAM = components[0]  # Assuming the first component is the team name
            if "N" in TEAM:
                print(line.strip())  # Print the entire line if the team name contains "N"
                
"""
4. Create a file called olympic-medals-5.csv that will contain only countries that have at least 5 gold medals.
"""
# Create olympic-medals-5.csv with countries that have at least 5 gold medals

with open("olympic-medals.csv", 'r') as source_file:
    lines = source_file.readlines()

with open("olympic-medals-5.csv", 'w') as destination_file:
    for line in lines:
        components = line.strip().split(',')  # Adjust delimiter if necessary
        if len(components) > 1:
            try:
                gold_medals = int(components[1])  # Assuming the gold medal count is in the second column
                if gold_medals >= 5:
                    destination_file.write(line)
            except ValueError:
                # Handle the case where the gold medal count is not an integer
                pass

# Print the contents of olympic-medals-5.csv to verify
with open("olympic-medals-5.csv", 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.strip())

"""
5. BONUS Create a file called olympic-medals-total10.csv that will contain only countries that have a total of
at least 10 medals of any kind.
"""
# Create olympic-medals-10.csv with countries that have at least 5 gold medals

with open("olympic-medals.csv", 'r') as source_file:
    lines = source_file.readlines()

with open("olympic-medals-10.csv", 'w') as destination_file:
    for line in lines:
        components = line.strip().split(',')  # Adjust delimiter if necessary
        if len(components) > 1:
            try:
                gold_medals = int(components[1])  # Assuming the gold medal count is in the second column
                siliver_medals = int(components[2])
                bronze_medals = int(components[3])
                if gold_medals + siliver_medals + bronze_medals  >= 10 :
                    destination_file.write(line)
            except ValueError:
                # Handle the case where the gold medal count is not an integer
                pass
# Print the contents of olympic-medals-5.csv to verify
with open("olympic-medals-10.csv", 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.strip())
"""
6. BONUS Create a different file for each country, called {COUNTRY}.txt (for example, Sweden.txt). The file will
contain the total number of medals this country has won.
"""
import os

input_filename = "olympic-medals.csv"

# Create a directory for the output files if it doesn't exist
output_directory = "country_medals"
os.makedirs(output_directory, exist_ok=True)

# Read the input file
with open(input_filename, 'r') as source_file:
    # Skip the header if there is one
    header = source_file.readline()
    
    # Dictionary to store total medals by country
    country_medals = {}
    
    # Process each line in the input file
    for line in source_file:
        components = line.strip().split(',')
        if len(components) >= 4:
            country = components[0].strip()
            try:
                gold = int(components[1].strip())
                silver = int(components[2].strip())
                bronze = int(components[3].strip())
                total_medals = gold + silver + bronze
                country_medals[country] = total_medals
            except ValueError:
                # Handle the case where medal counts are not integers
                pass

# Write each country's total medals to a separate file
for country, total_medals in country_medals.items():
    filename = os.path.join(output_directory, f"{country}.txt")
    with open(filename, 'w') as file:
        file.write(f"Total medals for {country}: {total_medals}\n")

# Print the created files and their contents
for country in country_medals.keys():
    filename = os.path.join(output_directory, f"{country}.txt")
    with open(filename, 'r') as file:
        print(file.read().strip())



###### Reading Binary Files ############################################################################################
"""
1. Create a copy of baseball.jpg under the name baseball-copy.jpg. Open the copy to see that it was copied succesfuly.
"""
with open("baseball.jpg", 'rb') as file:
	data = file.read()

with open("baseball-copy.jpg", 'wb') as file:
	file.write(data)

"""

2. Create a version of the sample.mp3 called sample-twice.mp3, so that the sound repeats twice! To do that, just
duplicated the content of the file. For example, if the content of sample.mp3 is X, then the new content is XX.
It should now be 6 seconds long instead of 3. Open the mp3 file and listen to it!
"""

with open("sample.mp3", 'rb') as file:
	contents = file.read()

with open("sample-twice.mp3", 'wb') as file:
	file.write(contents)
	file.write(contents)
"""
3. Create a copy of baseball.jpg under the name baseball-part.jpg that contains only the first 30,000 “characters”
of the file. Open the new picture. Did you see the effect of saving only part of the data?
"""

with open("baseball.jpg", 'rb') as file:
	data = file.read()

with open("baseball-part.jpg", 'wb') as file:
	file.write(data[:300000000])
	
################################## 1.9. (Bonus) Using External Libraries ###############################################


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
	"""
    Reads text from specific pages of a PDF file.
    :param file_path: Path to the PDF file.
    :param pages: List of page numbers to extract text from (1-indexed). If None, extracts all pages.
    :return: Extracted text from specified pages.
    """
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


#######################################################################################################################
"""
1.9.3. BONUS Writing a reproduced PDF
3. Create a new PDF file that contains only the first page.
"""

import PyPDF2
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch


def read_pdf(file_path, pages=None):
    """
    Reads text from specific pages of a PDF file.
    :param file_path: Path to the PDF file.
    :param pages: List of page numbers to extract text from (1-indexed). If None, extracts all pages.
    :return: Extracted text from specified pages.
    """
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

    """
    Writes text to a new PDF file with word wrapping to fit within margins on an A4 page.

    :param output_path: Path to the output PDF file.
    :param text: Text to be written to the PDF file.

    """

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
4. The last page of the PDF is rotated by accident. Save a new pdf file where the last page is rotated back so it’s
readable again.
"""

import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch


def read_and_rotate_pdf(input_path, output_path, pages=None, rotation=90):
    """
    Reads text from specific pages of a PDF file, rotates those pages, and writes the result to a new PDF file.

    :param input_path: Path to the input PDF file.
    :param output_path: Path to the output PDF file.
    :param pages: List of page numbers to rotate (1-indexed). If None, rotates all pages.
    :param rotation: Degrees to rotate pages (clockwise). Must be one of 90, 180, 270.
    """
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
	"""
    Reads text from specific pages of a PDF file.

    :param file_path: Path to the PDF file.
    :param pages: List of page numbers to extract text from (1-indexed). If None, extracts all pages.
    :return: Extracted text from specified pages.
    """
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
	"""
    Writes text to a new PDF file with word wrapping to fit within margins on an A4 page.

    :param output_path: Path to the output PDF file.
    :param text: Text to be written to the PDF file.
    """
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
"""
5. Reproduce a new PDF with a watermark applied to all of the pages. Use this watermark PDF. The final output should
 look like this:
"""
#######################################################################################################################

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




















