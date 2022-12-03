from pdf2jpg import pdf2jpg
from PIL import Image
from moviepy.editor import VideoFileClip


def ImageToPNG(file):
    filename = file.split(".")
    new_name = filename[0] + "_converted.png"
    img = Image.open(file)
    converted_img = img.convert("RGB")
    converted_img.save(new_name)


def pdfToPNG(file):
    filename = file.rsplit("/", 1) # Splits string on last occurrence of delimiter slash bar 
    outputpath = filename[0]
    result = pdf2jpg.convert_pdf2jpg(file, outputpath, pages="ALL")


def toGIF(file):
    toBeGif = VideoFileClip(file)
    filename = file.split(".")
    new_name = filename[0] + "_converted.gif"
    toBeGif.write_gif(new_name)
    toBeGif.close()
