from components.board import BoardFrame
from components.mainmenu import MainMenuFrame
from components.results import ResultsFrame
from components.root import RootFrame
from tkinter import Tk

def centerWindow(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    centerX = (screen_width - width) // 2
    centerY = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{centerX}+{centerY}")

def main():
    r = Tk()
    r.title("pydle")

    width = 300
    height = 256
    centerWindow(r, 500, 356)

    r.columnconfigure(0, weight=1)
    r.rowconfigure(0, weight=1)

    root = RootFrame(r)
    resultsFrame = ResultsFrame(root)
    boardFrame = BoardFrame(root)
    mainMenuFrame = MainMenuFrame(root)

    mainMenuFrame.playButton.config(command=lambda: mainMenuFrame.setupGame(r))

    resultsFrame.setBoardFrame(boardFrame)
    mainMenuFrame.setBoardFrame(boardFrame)
    boardFrame.setResultFrame(resultsFrame)

    resultsFrame.grid_remove()
    boardFrame.grid_remove()
    mainMenuFrame.grid(row=0, column=0)

    r.mainloop()

if __name__ == "__main__":
    main()
