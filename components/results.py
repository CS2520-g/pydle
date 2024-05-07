from tkinter import *
from tkinter import ttk
from components.Result import Result
from dictionary import *

class ResultsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        self.annoucementLabel = ttk.Label(self, text="Results", font=("Arial", 24))
        self.annoucementLabel.grid(row=0, column=0, columnspan=2)
        tryagain = ttk.Label(self, text="Try again?", font=("Arial", 18))
        tryagain.grid(row=1, column=0, columnspan=2)

    
        sizes = wordrange()
        buttonStyle = ttk.Style()
        buttonStyle.configure('restart.TButton', font=("Arial", 18))
        self.playButton = ttk.Button(self, command=self.setupGame, text="Start", style='restart.TButton')
        self.playButton.grid(row=2, column=0, columnspan=2, pady=5)
        self.optionLength = IntVar()
        self.optionLength.set(5)
        self.lengthLabel = ttk.Label(self, text="Length of word: ", font=("Arial", 18))
        self.lengthLabel.grid(row=3, column=0)
        self.chrSpinbox = ttk.Spinbox(self, from_=sizes[0], to=sizes[1], width=10, textvariable=self.optionLength, font=("Arial", 18))
        self.chrSpinbox.grid(row=3, column=1)
    
    def setBoardFrame(self, boardFrame: ttk.Frame):
        self.boardFrame = boardFrame

    def setupGame(self, *args):
        word = random_word(length=self.optionLength.get())
        self.boardFrame.setupGame(word)
        self.grid_remove()
        self._window.geometry(f"{600}x{500}+{self._window.winfo_x()}+{self._window.winfo_y()}")
        self.boardFrame.setWindow(self._window)
        self.boardFrame.grid()

    def setStatus(self, res: Result, expected: str):
        if res == Result.FAILURE:
            self.annoucementLabel.config(text=f"Game Over: word was {expected}", font=("Arial", 18))
        else:
            self.annoucementLabel.config(text=f"Congratulations! word was {expected}", font=("Arial", 18))

    def setWindow(self, r: Tk):
        self._window = r