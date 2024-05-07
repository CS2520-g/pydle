from tkinter import *
from tkinter import ttk

from components.Result import Result
from components.results import ResultsFrame
from dictionary import match_encode, CharacterMatch

class BoardFrame(ttk.Frame):
    def __init__(self, root: ttk.Frame):
        super().__init__(root)
        self.parent = root
        self.grid(sticky=NSEW)
        self.containerFrame = ttk.Frame(self)
        self.containerFrame.grid(row=1, sticky=NSEW)
        self.maxAttempts = 5
        self.remainingAttempts = IntVar()
        self.remainingAttempts.set(self.maxAttempts)
        self.remainingAttemptsLabel = ttk.Label(self, text=f"Remaining attempts: {self.remainingAttempts.get()}", font=("Arial", 18))
        self.remainingAttemptsLabel.grid(row=0)
        self.cells = []
        self.currentAttempt = 0
        self.wordFeedbackVar = StringVar()
        self.wordFeedbackLabel = ttk.Label(self, textvariable=self.wordFeedbackVar, font=("Arial", 18))
        # self.wordFeedbackLabel.grid(row=8)
        self.wordguess = StringVar()
        self.wordEntryBox = ttk.Entry(self, textvariable=self.wordguess, font=("Arial", 18)) 
        self.wordEntryBox.bind("<Return>", lambda *args: self.__validate(self.wordguess.get()))
        # self.wordEntryBox.grid(row=10)
        # self.wordEntryBox.focus()


    def __board_init(self) -> list[ttk.Frame]:
        self.remainingAttemptsLabel.grid(row=0)
        cells = []
        for i in range(self.maxAttempts):
            row = []
            for j in range(self.wordLength):
                f = Frame(self.containerFrame, relief=RIDGE, width=50, height=50, borderwidth=1)
                f.grid(row=i+1, column=j)
                f.grid_propagate(0)
                f.rowconfigure(0, weight=1)
                f.columnconfigure(0, weight=1)
                row.append(f)
            cells.append(row)

        self.wordFeedbackLabel.grid(row=self.maxAttempts)
        self.wordEntryBox.grid(row=self.maxAttempts + 1)
        return cells

    def setupGame(self, word: str):
        for listframe in self.cells:
            for frame in listframe:
                for child in frame.winfo_children():
                    child.destroy()
                frame.destroy()

        self.wordLength = len(word)
        self.word = word
        self.cells = self.__board_init()
        self.wordguess.set("")
        self.currentAttempt = 0
        self.remainingAttempts.set(self.maxAttempts)
        self.remainingAttemptsLabel.configure(text=f"Remaining attempts: {self.remainingAttempts.get()}", font=("Arial", 18))
        # self.wordEntryBox.focus()
    
    def __display_result(self, guess, match_res: list[CharacterMatch]):
        guess = guess.upper()
        
        for (i, frame) in enumerate(self.cells[self.currentAttempt]):
            letter = ttk.Label(frame, text=guess[i])
            
            match match_res[i]:
                case CharacterMatch.FULL_MATCH:
                    frame.configure(bg="green")
                    letter.configure(background="green")
                case CharacterMatch.WRONG_PLACE:
                    frame.configure(bg="yellow")
                    letter.configure(background="yellow")
                case CharacterMatch.NO_MATCH:
                    frame.configure(bg="black")
                    letter.configure(background="black")
                    
            if match_res[i] == CharacterMatch.NO_MATCH:
                letter.configure(foreground="white")
            
            letter.grid(row=0)


    def __validate(self, answer: str):
        if (len(answer) != self.wordLength):
            self.wordFeedbackVar.set("Incorrect amount of characters")
            return
        match_res = match_encode(self.word, answer)
        full_match = False

        for mtch in match_res:
            if mtch != CharacterMatch.FULL_MATCH:
                break
        else:
            full_match = True

        if full_match:
            self.__result_raise(Result.SUCCESS)
        else:
            self.__display_result(answer, match_res)
            self.currentAttempt += 1
            self.remainingAttempts.set(self.remainingAttempts.get() - 1)
            self.remainingAttemptsLabel.config(text=f"Remaining attempts: {self.remainingAttempts.get()}", font=("Arial", 18))

        if self.currentAttempt >= self.maxAttempts:
            self.__result_raise(Result.FAILURE)
        
    def __result_raise(self, res: Result):
            self.grid_remove()
            self.resultsFrame.setStatus(res, self.word)
            self._window.geometry((f"{400}x{256}+{self._window.winfo_x()}+{self._window.winfo_y()}"))
            self.resultsFrame.setWindow(self._window)
            self.resultsFrame.grid()

    def setResultFrame(self, frame: ResultsFrame):
        self.resultsFrame = frame

    def setWindow(self, r: Tk):
        self._window = r