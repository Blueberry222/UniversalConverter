# This project involves using multiple libraries to convert my most frequent needed files.
# Convert ideas: WEBP to PNG, PDF to PNG, WEBM to MP4, WEBP to GIF, MP4 to GIF,
# A GUI and upload function would be nice.

from PIL import Image
import os
import sys

fileToConvert = "D:\Pictures\\test.jpeg"


def toPNG(file):
    filename = file.split(".")
    img = Image.open(file)
    new_name = filename[0] + "_converted.png"
    converted_img = img.convert("RGB")
    converted_img.save(new_name)


toPNG(fileToConvert)
