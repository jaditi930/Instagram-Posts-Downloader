from tkinter import *
from insta_downloader import *

def myfunc(arg):
    if arg==option_list[0]:
        Label(text="Enter Username:").place(relx=0.4,rely=0.3)
        Entry(textvariable=Username).place(relx=0.4,rely=0.4)
        # username=
        # print(username)
        submit_btn=Button(text="Download",command=lambda:download_profile(username=Username.get()),bg="light green")
        submit_btn.place(relx=0.4,rely=0.8)
        
    else:
        Label(text="Enter Url of post to download:").place(relx=0.4,rely=0.3)
        Entry(textvariable=Url).place(relx=0.4,rely=0.4)
        shortcode=Url.get().split("/")[4]
        submit_btn=Button(text="Download",command=lambda:downloadSpecific(shortcode),bg="light green")
        submit_btn.place(relx=0.4,rely=0.8)

window=Tk()
window.geometry("644x434")
window.title("Instagram Posts Downloader")
text=Label(text="INSTAGRAM POSTS DOWNLOADER",font=("Helventica", "20", "bold"),fg="white",bg="red",padx=10,pady=10)
text.place(relx=0.1,rely=0.1)
user_choice=Label(text="Select an option:",font="Helventica 15 bold")
user_choice.place(relx=0.2,rely=0.3)
ChoiceVal=StringVar()
Username=StringVar()
Url=StringVar()

ChoiceVal.set("Select an option")
option_list=["Download profile pic","Download posts,videos or reels"]
option_menu=OptionMenu(window,ChoiceVal,*option_list,command=myfunc)
option_menu.place(relx=0.5,rely=0.3)
window.mainloop()