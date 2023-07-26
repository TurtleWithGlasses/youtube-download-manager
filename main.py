from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import re
import threading


class Application:

    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(bg="light gray")

        top_label = Label(self.root, text="YouTube Download Manager", fg="orange", font=("Arial", 50))
        top_label.grid(pady=(0, 10))

        link_label = Label(self.root, text="Paste below any YouTube video link", font=("SnowPersons", 30))
        link_label.grid(pady=(0,20))

        self.link_entry_var = StringVar()
        self.link_entry = Entry(self.root, width=70, textvariable=self.link_entry_var, font=("Agency Fb",25), fg="blue")
        self.link_entry.grid(pady=(0,15), ipady=2)

        self.link_entry_error = Label(self.root, text="", font=("Concert One", 20))
        self.link_entry_error.grid(pady=(0, 8))

        self.file_save_label = Label(self.root, text="Choose Directory", font=("Concert One", 30))
        self.file_save_label.grid()

        self.file_save_button = Button(self.root, text="Save", font=("Bell MY", 15), command=self.open_directory)
        self.file_save_button.grid(pady=(10, 3))


if __name__ == "__main__":
    window = Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)


    mainloop()