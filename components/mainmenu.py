from tkinter import *
from tkinter import ttk
from dictionary import *


class MainMenuFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        sizes = wordrange()

        basicTextStyle = ttk.Style()
        basicTextStyle.configure('start.TButton', font=("Arial", 18))

        self.welcomeLabel = ttk.Label(self, text="Welcome to Pydle!", font=("Arial", 24))
        self.welcomeLabel.grid(row=0, columnspan=2, pady=10)
        self.playButton = ttk.Button(self, command=self.setupGame, text="Start", style='start.TButton')
        self.playButton.grid(row=3, columnspan=2, pady=10)
        self.playButton.bind("<Return>", lambda: self.setupGame)
        basicTextStyle.configure('start.TButton', font=("Arial", 18))
 
        self.optionLength = IntVar()
        self.optionLength.set(5)

        self.chrSpinbox = ttk.Spinbox(self, from_=sizes[0], to=sizes[1], width=5 , textvariable=self.optionLength, font=("Arial", 18))
        self.chrSpinbox.grid(row=1, column=1)

        self.lengthLabel = ttk.Label(self, text="Length of word:", font=("Arial", 18))
        self.lengthLabel.grid(row=1, column=0)
    
    def setBoardFrame(self, boardFrame):
        self.boardFrame = boardFrame

    def setupGame(self, *args):
        word = random_word(length=self.optionLength.get())
        self.grid_remove()
        self.boardFrame.setupGame(word)
        self.boardFrame.grid()