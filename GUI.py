from tkinter import *
from tkinter import ttk
from main import *


# https://tkdocs.com/tutorial/concepts.html
def test():
    print("Helloo!!!")

class MainGui:
    def __init__(self, root):

        root.title("Universal Converter")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Select file to convert:").grid(column=1, row=1, sticky=W)
        # Insert upload here

        ttk.Button(mainframe, text="Upload", command=test).grid(column=2, row=1, sticky=W)


        # walks through all of the widgets contained within our content frame and adds a little bit of padding around each
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)



root = Tk()
MainGui(root)
root.mainloop()
