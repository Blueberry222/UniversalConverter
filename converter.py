from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip


def ImageToPNG(file):
    filename = file.split(".")
    new_name = filename[0] + "_converted.png"
    img = Image.open(file)
    converted_img = img.convert("RGB")
    converted_img.save(new_name)


def toGIF(file):
    toBeGif = VideoFileClip(file)
    filename = file.split(".")
    new_name = filename[0] + "_converted.gif"
    toBeGif.write_gif(new_name)
    toBeGif.close()
