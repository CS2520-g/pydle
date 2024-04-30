from tkinter import *
from tkinter import ttk
from components.Result import Result
from dictionary import *

class ResultsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        self.annoucementLabel = ttk.Label(self, text="Results")
        self.annoucementLabel.grid(row=0)
        tryagain = ttk.Label(self, text="Try again?")
        tryagain.grid(row=1)

    
        sizes = wordrange()
        self.playButton = ttk.Button(self, command=self.setupGame, text="Start")
        self.playButton.grid(row=2)
        self.optionLength = IntVar()
        self.optionLength.set(5)
        self.lengthLabel = ttk.Label(self, text="Length of word: ")
        self.lengthLabel.grid(row=3)
        self.chrSpinbox = ttk.Spinbox(self, from_=sizes[0], to=sizes[1], textvariable=self.optionLength)
        self.chrSpinbox.grid(row=4)
    
    def setBoardFrame(self, boardFrame: ttk.Frame):
        self.boardFrame = boardFrame

    def setupGame(self, *args):
        word = random_word(length=self.optionLength.get())
        self.boardFrame.setupGame(word)
        self.grid_remove()
        self.boardFrame.grid()

    def setStatus(self, res: Result, expected: str):
        if res == Result.FAILURE:
            self.annoucementLabel.config(text=f"Game over: word was {expected}")
        else:
            self.annoucementLabel.config(text=f"Congratulations! word was {expected}")

