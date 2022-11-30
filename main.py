# This project involves using multiple libraries to convert my most frequent needed files.
# Convert ideas:
#  WEBP to PNG [x]
#  PDF to PNG [x]
#  WEBP to GIF [x]
#  MP4 to GIF [x]
# A GUI and upload function would be nice.

import aspose.words as aw
from PIL import Image
from moviepy.editor import VideoFileClip  # pip install moviepy

fileToConvert = 'D:\Downloads\\Young Kitsuragi.jpg'


def toPNG(file):
    if file.endswith(".webp") or file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".tiff"):
        filename = file.split(".")
        new_name = filename[0] + "_converted.png"
        img = Image.open(file)
        converted_img = img.convert("RGB")
        converted_img.save(new_name)

    if file.endswith(".pdf"):
        filename = file.split(".")
        pdf = aw.Document(file)
        for page in range(0, pdf.page_count):
            extractedPage = pdf.extract_pages(page, 1)
            new_name = filename[0] + f"converted_{page + 1}.png"
            extractedPage.save(new_name)


def toGIF(file):
    if file.endswith(".webm") or file.endswith(".mp4"):
        toBeGif = VideoFileClip(file)
        filename = file.split(".")
        new_name = filename[0] + "_converted.gif"
        toBeGif.write_gif(new_name)
        toBeGif.close()


toPNG(fileToConvert)
