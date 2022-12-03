import aspose.words as aw
from PIL import Image
from moviepy.editor import VideoFileClip


def ImageToPNG(file):
    filename = file.split(".")
    new_name = filename[0] + "_converted.png"
    img = Image.open(file)
    converted_img = img.convert("RGB")
    converted_img.save(new_name)


def pdfToPNG(file):
    filename = file.split(".")
    pdf = aw.Document(file)
    for page in range(0, pdf.page_count):
        extractedPage = pdf.extract_pages(page, 1)
        new_name = filename[0] + f"converted_{page + 1}.png"
        extractedPage.save(new_name)


def toGIF(file):
    toBeGif = VideoFileClip(file)
    filename = file.split(".")
    new_name = filename[0] + "_converted.gif"
    toBeGif.write_gif(new_name)
    toBeGif.close()
