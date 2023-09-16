from tkinter import *
from insta_downloader import *

def clear_frame(frm):
   for widgets in frm.winfo_children():
      widgets.destroy()

def myfunc(arg):
    title.config(text=choice_list[arg])
    if arg==0:
        label.config(text="Enter username:")
        entry.config(textvariable=Username)
        dwld_btn.config(command=lambda:dp(username=Username.get()))
        
    elif arg==1:
        label.config(text="Enter url:")
        entry.config(textvariable=Url)
        dwld_btn.config(command=lambda:ds(Url.get().split("/")[4],"reels"))

    label.pack(in_=f2,side=LEFT,anchor=W)
    entry.pack(in_=f2,side=RIGHT,anchor=W)
    dwld_btn.pack(in_=f3)
    f2.pack()
    f3.pack()

window=Tk()
window.geometry("944x634")
window.title("Instagram Posts Downloader")
text=Label(text="INSTAGRAM POSTS DOWNLOADER",font=("Helventica", "20", "bold"),fg="black",padx=10,pady=5)
text.pack()

choice_list=["DOWNLOAD PROFILE PHOTO","DOWNLOAD A POST, VIDEO OR REEL","DOWNLOAD ALL POSTS"]

f1=Frame()
f1.pack(side=TOP)

b1=Button(text="DOWNLOAD PROFILE PHOTO",font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:myfunc(0))
b2=Button(text="DOWNLOAD A POST, VIDEO OR REEL",font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:myfunc(1))
b3=Button(text="DOWNLOAD ALL POSTS",font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:myfunc(2))

b1.pack(in_=f1, side=LEFT)
b2.pack(in_=f1, side=LEFT)
b3.pack(in_=f1, side=LEFT)

title=Label(text="",font=("Times New Roman", "15","italic"),padx=15,pady=15)
title.pack(anchor=W)

f2=Frame()

f3=Frame()

label=Label(text="",font=("Helventica", "15"))
entry=Entry(font=("Helventica", "15"))
dwld_btn=Button(text="Download",bg="light green",padx=5,pady=5,font=("15"))


Username=StringVar()
Url=StringVar()
 
window.mainloop()