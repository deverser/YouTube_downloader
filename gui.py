from tkinter import *


def clicked():
    res = txt.get()
    lbl.configure(text=res)


window = Tk()
window.title("YouTube downloader")
window.geometry('700x300')
lbl = Label(window, text="Вставьте ссылку на видео YouTube: ")
lbl.grid(column=0, row=0)
txt = Entry(window, width=50)
txt.grid(column=1, row=0)
btn = Button(window, text="Download", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
