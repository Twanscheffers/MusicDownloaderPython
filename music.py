import os
from pytube import YouTube
from tkinter import *
from tkinter import filedialog as fd

def openFolder():
    #function for opening folder path for download location
    global folder_path
    pathname = fd.askdirectory()
    folder_path.set(pathname)
    print(folder_path.get())

def myClick():
    #function for downloading MP3
    yt = YouTube(e.get())
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=folder_path.get())
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

root = Tk()
root.geometry("400x160")
root.resizable(False, False)
e = Entry(root, width=50, borderwidth=2)
e.pack()

folder_path = StringVar()
myCanvas = Canvas(root, height=100, width=400, bg="#FFFFFF").pack()
downloadButton = Button(root, text = "Download", width=24, command=myClick).place(x=1, y=127)
pathButton = Button(root, text="Browse path", width=24, command=openFolder).place(x=200, y=127)
label2 = Label(root, text="Dit is een test", height=600).pack()

root.mainloop()