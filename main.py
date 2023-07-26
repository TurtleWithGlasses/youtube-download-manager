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

        self.file_save_button = Button(self.root, text="Directory", font=("Bell MY", 15), command=self.open_directory)
        self.file_save_button.grid(pady=(10, 3))

        self.file_location_label = Label(self.root, text="", font=("Freestyle Script", 25))
        self.file_location_label.grid()

        self.choose_download_type = Label(self.root, text="Choose download type", font=("Variety",30))
        self.choose_download_type.grid()

        self.download_choice = [("Audio MP3", 1), ("Video MP4", 2)]
        self.choice_var = StringVar()
        self.choice_var.set(1)

        for text, mode in self.download_choice:
            self.youtube_choice = Radiobutton(self.root, text=text, font=("Northwest old", 25), variable=self.choice_var, value=mode)
            self.youtube_choice.grid()

        self.download_button = Button(self.root, text="Download", width=10, font=("Bell MT", 15), command=check_youtube_link())
        self.download_button.grid(pady=(30,5))


    def check_youtube_link(self):

        self.match_link = re.match("^https://www.youtube.com/.",self.link_entry_var.get())
        if not self.match_link:
            self.link_entry_error.config(text="Invalid YouTube Link", fg="red")
        elif not self.open_directory():
            self.file_location_label.config(text="Please choose a correct directory", fg="red")
        elif self.match_link and self.file_location_label:
            self.download_window()


    def download_window(self):
        self.download_file_window = Toplevel(self.root)
        self.root.withdraw()

        self.app = SecondApp(self.download_file_window, self.link_entry_var.get(), self.file_name.get(), self.choice_var.get())




    def open_directory(self):
        self.file_name = filedialog.askdirectory()

        if len(self.file_name) > 0:
            self.file_location_label.config(text=self.file_name, fg="green")
            return True
        else:
            self.file_location_label.config(text="Please choose a directory", fg="red")


if __name__ == "__main__":
    window = Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)


    mainloop()