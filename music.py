import os
from pytube import YouTube
from tkinter import *
from tkinter import filedialog as fd

def openFile():
    global folder_path
    pathname = fd.askdirectory()
    folder_path.set(pathname)
    print(folder_path.get())

def myClick():
    #maak een functie die de download start en de link pakt uit de entry e
    yt = YouTube(e.get())
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=folder_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


root = Tk()
e = Entry(root, width=50, borderwidth=2)
e.pack()

folder_path = StringVar()
#test commit de laatste poging vandaag
myCanvas = Canvas(root, height=100, width=400, bg="#263D42")
myCanvas.pack()
myButton1 = Button(root, text = "Download", command=myClick)
myButton1.pack()
myButton2 = Button(root, text="Browse path", command=openFile)
myButton2.pack()

root.mainloop()