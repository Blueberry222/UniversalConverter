from PIL import Image, ImageSequence
from moviepy.video.io.VideoFileClip import VideoFileClip


def toPNG(file):
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


def webpConversion(file):
    MediaFile = Image.open(file)

    Index = 0

    for Frames in ImageSequence.Iterator(MediaFile):
        Index += 1

    if Index > 1:  # .webp is a gif because it has more than one frame
        webp = Image.open(file)
        filename = file.split(".")
        new_name = filename[0] + "_converted.gif"
        webp.info.pop('background', None)
        webp.save(new_name, 'gif', save_all=True)

    else:  # webp has 1 frame which makes it an image
        toPNG(file)
        print("Teste")
