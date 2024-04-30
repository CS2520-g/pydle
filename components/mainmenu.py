from tkinter import *
from tkinter import ttk
from dictionary import *


class MainMenuFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        sizes = wordrange()
        self.welcomeLabel = ttk.Label(self, text="Welcome")
        self.welcomeLabel.grid(row=0)
        self.playButton = ttk.Button(self, command=self.setupGame, text="Start")
        self.playButton.grid(row=3)
        self.optionLength = IntVar()
        self.optionLength.set(5)
        self.chrSpinbox = ttk.Spinbox(self, from_=sizes[0], to=sizes[1], textvariable=self.optionLength)
        self.chrSpinbox.grid(row=2)
        self.lengthLabel = ttk.Label(self, text="Length of word:")
        self.lengthLabel.grid(row=1)
        self.playButton.bind("<Return>", lambda: self.setupGame)
    
    def setBoardFrame(self, boardFrame):
        self.boardFrame = boardFrame

    def setupGame(self, *args):
        word = random_word(length=self.optionLength.get())
        self.grid_remove()
        self.boardFrame.setupGame(word)
        self.boardFrame.grid()