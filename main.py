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

        self.YouTubeEntryVar = StringVar()
        self.YouTubeEntry = Entry(self.root, width=70, textvariable=self.YouTubeEntryVar, font=("Agency Fb",25), fg="blue")
        self.YouTubeEntry.grid(pady=(0,15), ipady=2)

        self.YouTubeEntryError = Label(self.root, text="", font=("Concert One", 20))
        self.YouTubeEntryError.grid(pady=(0, 8))

        self.YouTubeFileSaveLabel = Label(self.root, text="Choose Directory", font=("Concert One", 30))
        self.YouTubeFileSaveLabel.grid()

        self.youtubeFileDirectoryButton = Button(self.root, text="Directory", font=("Bell MY", 15), command=self.openDirectory)
        self.youtubeFileDirectoryButton.grid(pady=(10, 3))

        self.fileLocationLabel = Label(self.root, text="", font=("Freestyle Script", 25))
        self.fileLocationLabel.grid()

        self.youtubeChooseLabel = Label(self.root, text="Choose download type", font=("Variety", 30))
        self.youtubeChooseLabel.grid()

        self.downloadChoices = [("Audio MP3", 1), ("Video MP4", 2)]
        self.ChoiceVar = StringVar()
        self.ChoiceVar.set(1)

        for text, mode in self.downloadChoices:
            self.youtubeChoices = Radiobutton(self.root, text=text, font=("Northwest old", 25), variable=self.ChoiceVar, value=mode)
            self.youtubeChoices.grid()

        self.downloadButton = Button(self.root, text="Download", width=10, font=("Bell MT", 15), command=self.checkYoutubeLink)
        self.downloadButton.grid(pady=(30,5))


    def checkYoutubeLink(self):

        self.matchYoutubeLink = re.match("^https://www.youtube.com/.", self.YouTubeEntryVar.get())
        if not self.matchYoutubeLink:
            self.YouTubeEntryError.config(text="Invalid YouTube Link", fg="red")
        elif not self.openDirectory:
            self.fileLocationLabel.config(text="Please choose a correct directory", fg="red")
        elif self.matchYoutubeLink and self.openDirectory:
            self.downloadWindow()


    def downloadWindow(self):
        self.newWindow = Toplevel(self.root)
        self.root.withdraw()
        self.newWindow.state("zoomed")
        self.newWindow.grid_rowconfigure(0, weight=0)
        self.newWindow.grid_columnconfigure(0, weight=1)

        self.app = DownloadApp(self.newWindow, self.YouTubeEntryVar.get(), self.FolderName, self.ChoiceVar.get())


    def openDirectory(self):
        self.FolderName = filedialog.askdirectory()

        if len(self.FolderName) > 0:
            self.fileLocationLabel.config(text=self.FolderName, fg="green")
            return True
        else:
            self.fileLocationLabel.config(text="Please choose a directory", fg="red")


class DownloadApp:

    def __init__(self, downloadWindow, youtubeLink, FolderName, Choices):
        self.downloadWindow = downloadWindow
        self.youtubeLink = youtubeLink
        self.FolderName = FolderName
        self.Choices = Choices

        self.yt = YouTube(self.youtubeLink)

        if Choices == "1":
            self.video_type = self.yt.streams.filter(only_audio=True).first()
            self.MaxFileSize = self.video_type.filesize

        if Choices == "2":
            self.video_type = self.yt.streams.first()
            self.MaxFileSize = self.video_type.filesize

        self.loading_label = Label(self.downloadWindow, text="Downloading...", font=("Arial", 40))
        self.loading_label.grid(pady=(100, 0))

        self.loading_percentage = Label(self.downloadWindow, text="0", fg="green", font=("Arial", 40))
        self.loading_percentage.grid(pady=(50, 0))

        self.progressbar = ttk.Progressbar(self.downloadWindow, length=500, orient="horizontal", mode="undetermined")
        self.progressbar.grid(pady=(50, 0))
        self.progressbar.start()



if __name__ == "__main__":
    window = Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)


    mainloop()