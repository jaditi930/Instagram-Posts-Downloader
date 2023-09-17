import instaloader
import threading
ig = instaloader.Instaloader()
from tkinter import *
from time import sleep

downloading=0 

def download(type):
    user_input=Userinput.get()

    # to download profile picture
    if type==0:
        ig.download_profile(user_input , profile_pic_only=True)

    # to download particular post,video or reel
    elif type==1:
        post = instaloader.Post.from_shortcode(ig.context,user_input)
        ig.download_post(post,target="downloads")

    # to download all posts of a user
    else:
        profile = instaloader.Profile.from_username(ig.context,user_input)

        for post in profile.get_posts():
            print(post.title)
            ig.download_post(post, target=profile.username)


    dwld_label.config(text="Downloading has completed successfully ...")
    sleep(1)
    dwld_label.config(text="Ready to Download ...")


def start_download(type):

    t1 = threading.Thread(target=download, args=(type,))
    t1.start()
    dwld_label.config(text="Downloading has started ...")


def update_gui(type):
    title.config(text=choice_list[type])
    entry.config(textvariable=Userinput)
    dwld_btn.config(command=lambda:start_download(type))

    if type==1:
        label.config(text="Enter url:")
        
    else:
        label.config(text="Enter username:")

    label.pack(in_=f2,side=LEFT,anchor=W)
    entry.pack(in_=f2,side=RIGHT,anchor=W)
    dwld_btn.pack(in_=f3)
    f2.pack()
    f3.pack()

window=Tk()
window.geometry("944x634")
window.title("Instagram Posts Downloader")

Userinput=StringVar()

text=Label(text="INSTAGRAM POSTS DOWNLOADER",font=("Helventica", "20", "bold"),fg="black",padx=10,pady=5)
text.pack()

choice_list=["DOWNLOAD PROFILE PHOTO","DOWNLOAD A POST, VIDEO OR REEL","DOWNLOAD ALL POSTS"]

f1=Frame()
f1.pack(side=TOP)

b1=Button(text=choice_list[0],font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:update_gui(0))
b2=Button(text=choice_list[1],font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:update_gui(1))
b3=Button(text=choice_list[2],font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:update_gui(2))

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

dwld_label=Label(text="Ready to Download ...",font=("Helventica", "15"))
dwld_label.pack(ipadx=5,ipady=5)
 
window.mainloop()