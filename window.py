from tkinter import filedialog
from imagetotext import processImagePath
import tkinter


def main():
    root = tkinter.Tk()
    root.geometry("500x500")
    root.pick_file = tkinter.Button(root)
    root.pick_file.pack(side="top")
    root.mainloop()


if __name__ == '__main__':
    main()
