from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from converter import *


def convertFile():
    file_path = filedialog.askopenfilename()

    if Path(file_path).suffix == '.webp' or Path(file_path).suffix == '.jpeg' or Path(file_path).suffix == '.jpg' or Path(file_path).suffix == '.tiff':
        ImageToPNG(file_path)

    elif Path(file_path).suffix == '.pdf':
        pdfToPNG(file_path)

    elif Path(file_path).suffix == '.webm' or Path(file_path).suffix == '.mp4':
        toGIF(file_path)

    else:
        messagebox.showerror('Erro', '"Nenhum arquivo selecionado / extensão inválida."')


class MainGui:
    def __init__(self, root):

        mainframe = ttk.Frame(root)
        root.resizable(False, False)
        root.title("Universal Converter")
        mainframe.grid(column=0, row=0, sticky=W)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text=" Universal Converter ", font="Cambria 16", borderwidth=2, relief="solid", anchor="center").grid(column=1, row=0, sticky=EW)
        ttk.Button(mainframe, text="Convert to PNG", command=lambda: convertFile()).grid(column=1, row=1, sticky=EW)
        #create progress bar
        #create text sidebar explaning the software

        # walks through all the widgets contained within our content frame and adds a bit of padding around each
        for child in mainframe.winfo_children():
            child.grid_configure(padx=3, pady=3)


root = Tk()
MainGui(root)
root.mainloop()
