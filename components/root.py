from tkinter import *
from tkinter import ttk

class RootFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()
        # mainf.grid(column=0,row=0, sticky=(N,S,E,W))

        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)