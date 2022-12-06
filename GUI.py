from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter.ttk import Style
from pathlib import Path
from converter import *


def convertFile():
    file_path = filedialog.askopenfilename()

    if Path(file_path).suffix == ".jfif" or Path(file_path).suffix == '.jpeg' or Path(file_path).suffix == '.jpg' or Path(file_path).suffix == '.tiff':
        toPNG(file_path)

    elif Path(file_path).suffix == '.webm' or Path(file_path).suffix == '.mp4':
        toGIF(file_path)

    elif Path(file_path).suffix == '.webp':
        webpConversionToPNG(file_path)

    elif Path(file_path).suffix == '.png':
        imageToWEBP(file_path)

    else:
        messagebox.showerror('Error', '"No file selected / invalid file extension."')


def helpButton():
    messagebox.showinfo("Help", "Upon clicking the option: 'Convert File' and selecting your file, it will automatically be converted to either a PNG image or a GIF file; "
                                "being save in the same place as the original file with _converted appended to it's name."
                                "\n"
                                "\n"
                                "You can convert the following files:\n"
                                "WEBP, JPEG, JPG, JFIF and TIFF to PNG"
                                "PNG, JPEG, JPG, JFIF and TIFF to WEBP \n"
                                "Animated WEBP and MP4 to GIF\n"
                                "\nThank you for using my little software!\n")


class MainGui:
    def __init__(self, root):

        mainframe = ttk.Frame(root)
        root.resizable(False, False)
        root.title("Universal Converter")
        mainframe.grid(column=0, row=0, sticky=W)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        s = Style()
        s.configure('TButton', font=('Cambria', 12, "bold"))

        ttk.Label(mainframe, text=" Universal Converter ", font="Cambria 16 bold", borderwidth=2, relief="solid", anchor="center").grid(column=1, row=0, sticky=EW)
        ttk.Button(mainframe, text="Convert File", command=lambda: convertFile()).grid(column=1, row=1, sticky=EW)
        ttk.Button(mainframe, text="?", style="TButton", width=2, command=lambda: helpButton()).grid(column=1, row=2, sticky=E)

        # walks through all the widgets contained within our content frame and adds a bit of padding around each
        for child in mainframe.winfo_children():
            child.grid_configure(padx=3, pady=3)


root = Tk()
MainGui(root)
root.mainloop()

