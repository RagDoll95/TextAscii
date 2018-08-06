from tkinter import filedialog
from imagetotext import processImagePath
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pick_file = tk.Button(self)
        self.pick_file["text"] = "Pick file"
        self.pick_file["command"] = self.get_file
        self.pick_file.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def get_file(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.master.destroy()
        processImagePath(self.filename)
        return self.filename
def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
