import instaloader
import threading
ig = instaloader.Instaloader()
from tkinter import *
from time import sleep

#https://www.instagram.com/reel/CxPwnKxMcvg/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==
downloading=0 
queue=[]

def download():
    global downloading
    downloading=1
    while len(queue)>0:
        item=queue.pop()
        user_input=item[0]
        type=item[1]
        print(user_input,type)

        try:
        # to download profile picture
            if type==0:
                ig.download_profile(user_input , profile_pic_only=True)

            # to download particular post,video or reel
            elif type==1:
                shortcode=user_input.split("/")[4]
                post = instaloader.Post.from_shortcode(ig.context,shortcode)
                ig.download_post(post,target="downloads")

            # to download all posts of a user
            else:
                profile = instaloader.Profile.from_username(ig.context,user_input)

                for post in profile.get_posts():
                    ig.download_post(post, target=profile.username)

            dwld_label.config(text="Downloading has completed successfully ...")

        except :
            dwld_label.config(text="Downloading failed ...")

    sleep(1)
    dwld_label.config(text="Ready to Download ...")
    downloading=0


def start_download(cancel=0):
    global queue
    if cancel==1:
        queue=[]
        return
    queue.append((Userinput.get(),Type.get()))
    if downloading==0:
        t1 = threading.Thread(target=download, args=())
        t1.start()
        dwld_label.config(text="Downloading has started ...")

    Userinput.set("")


def update_gui(type):
    Type.set(type)
    title.config(text=choice_list[type])

    if type==1:
        label.config(text="Enter url:")
        
    else:
        label.config(text="Enter username:")

window=Tk()
window.geometry("944x634")
window.minsize(944,634)
window.maxsize(944,634)
window.title("Instagram Posts Downloader")

Userinput=StringVar()
Type=IntVar()

text=Label(text="INSTAGRAM POSTS DOWNLOADER",font=("Helventica", "25", "bold"),fg="black",padx=10,pady=20)
text.pack()

choice_list=["DOWNLOAD PROFILE PHOTO","DOWNLOAD A POST, VIDEO OR REEL","DOWNLOAD ALL POSTS"]

f1=Frame()
f1.pack()

b1=Button(text=choice_list[0],font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:update_gui(0))
b2=Button(text=choice_list[1],font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:update_gui(1))
b3=Button(text=choice_list[2],font=("Helventica", "12", "bold"),padx=5,pady=5,command=lambda:update_gui(2))

b1.pack(in_=f1, side=LEFT)
b2.pack(in_=f1, side=LEFT)
b3.pack(in_=f1, side=LEFT)

title=Label(text=choice_list[Type.get()],font=("Helventica", "16","bold"),padx=15,pady=15,width=100)
title.pack()

f2=Frame()
f2.pack(ipadx=20,ipady=20)

label=Label(text="Enter username:",font=("Helventica", "15"))
entry=Entry(font=("Helventica", "15"),width=40,textvariable=Userinput)

label.pack(in_=f2,side=LEFT,anchor=W)
entry.pack(in_=f2,side=RIGHT,anchor=W)

f3=Frame()
f3.pack()

dwld_btn=Button(text="START DOWNLOAD",padx=5,pady=5,font=("Helventica","12","bold"),width=20,command=start_download)
dwld_btn.pack(in_=f3,side=LEFT)
cancel_btn=Button(text="CANCEL DOWNLOAD",padx=5,pady=5,font=("Helventica","12","bold"),width=20,command=lambda:start_download(1))
cancel_btn.pack(in_=f3,side=LEFT)

f4=Frame()
f4.pack(side=BOTTOM,anchor="sw")
dwld_label=Label(text="Ready to Download ...",font=("Helventica", "15"),width=100,bg="sky blue")
dwld_label.pack(in_=f4,ipadx=5,ipady=10)
 
window.mainloop()