# This project involves using multiple libraries to convert my most frequent needed files.
# Convert ideas:
#  WEBP to PNG [x]
#  PDF to PNG [x]
#  WEBM to MP4,
#  WEBP to GIF,
#  MP4 to GIF,
# A GUI and upload function would be nice.

import aspose.words as aw
from PIL import Image

fileToConvert = 'D:\Pictures\\JasperReportsIReport.pdf'


def toPNG(file):
    if file.endswith(".webp") or file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".tiff"):
        filename = file.split(".")
        img = Image.open(file)
        new_name = filename[0] + "_converted.png"
        converted_img = img.convert("RGB")
        converted_img.save(new_name)

    if file.endswith(".pdf"):
        filename = file.split(".")
        pdf = aw.Document(file)
        for page in range(0, pdf.page_count):
            extractedPage = pdf.extract_pages(page, 1)
            new_name = filename[0] + f"converted_{page + 1}.png"
            extractedPage.save(new_name)


# def toMP4(file):


toPNG(fileToConvert)
