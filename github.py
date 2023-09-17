from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from time import sleep
from os import listdir
from pytube.contrib.playlist import Playlist
import os
import threading

downloading = 0
queue = []
list=[]
temp_status=""
file_size=0
# functions
def clear_url_box():
    URL.set("")
def paste_url():
    URL.set(root.clipboard_get())
def select_folder():
    folder = filedialog.askdirectory()
    folder= os.path.join(folder,"Elite_youtube_downloader")
    download_path.set(folder)
    downloads_location.set(f"Downloads path :- {folder}")
    download_loacation_display.update()
def update_status(temp):
    statusvar.set(temp)
    sbar.update()
def update_percentage_status(temp):
    statusvar.set(f"{temp_status}\nDone : {int(temp*100)}%")
    sbar.update()
def progress(stream,chunk,byte_remaining):
    percent = (file_size-byte_remaining)/file_size
    update_percentage_status(percent)
def queue_playlist():
    link=URL.get()
    if link!="":
        queue.append([link,1])
        clear_url_box()
        start_downloadin()

def queue_only_video():
    link=URL.get()
    if link!="":
        queue.append([link,0])
        clear_url_box()
        start_downloadin()
    
def start_downloadin():
    if(downloading==0):
        t = threading.Thread(target=download_start)
        t.start()
def download_start():
    global downloading
    downloading = 1
    while(len(queue)!=0):
        print(len(queue))
        temp = queue.pop(0)
        if(temp[1]==0):
            download_only_video(temp[0])
        else:
            download_playlist(temp[0])
    downloading = 0

def download_playlist(link):
    print(link)
    update_status("Collecting information to download playlist.")
    try:
        playlist = Playlist(link)
        temp_title=playlist.title.replace('/','_')
    except:
        update_status("Enter valid link.")
        sleep(0.3)
        update_status("Ready to download")
        return
    temp_path=os.path.join(download_path.get(),temp_title)
    try:
        os.mkdir(temp_path)
    except:
        pass
    cur_path.set(temp_path)
    # print(playlist.length)
    i=1
    trials=0
    for p in playlist:
        # print(p)
        download_video(p,i,playlist.length)
        i=i+1
    # print(list)
    while not list:
        trials=trials+1
        if trials==10:
            break
        for p in list:
            download_video(p,i,playlist.length)
            i=i+1   
    list.clear()
    delete_list()
    update_status("Playlist Downloaded.")


# function to download video of playlists
def download_video(video_link,cur,last):
    global temp_status
    global file_size
    update_status(f"Checking video link {cur} out of {last}")
    if video_link!="":
        try:
            yt=YouTube(video_link,on_progress_callback=progress)
        except:
            list.append(video_link)
            return

        # print(yt)
        try:
            update_status(f"Collecting information to download video {cur} out of {last}")
            if download_in_audio_format.get():
                video = yt.streams.filter(only_audio=True).first()
                # print(video)
            else:
                video = yt.streams.filter(progressive=True,file_extension='mp4')
                video = video.get_highest_resolution()
        except:
            return
        # print(video)
        try:
            # downloading the video
            file_size=video.filesize
            temp_status=f"Downloading video {cur} out of {last}\nTitle:{video.title}\nSize:{video.filesize/1000000} MB"
            update_percentage_status(0)
            video.download(cur_path.get())
            # print(f"done {cur}")
            if video_link in list:
                list.remove(video_link)
        except:
            list.append(video_link)
            return
    else:
        return
def delete_list():
   mylist.delete(0,END)
   showfiles()
def showfiles():
    for video_file in listdir(download_path.get()):
        if video_file.endswith(".mp4"):
            mylist.insert(END," "+str("VIDEO/AUDIO FILE : "+video_file)) 
        elif os.path.isdir(os.path.join(download_path.get(),video_file)):
            mylist.insert(END," "+str("PLAYLIST : "+video_file))
             
# function to download indivisual video 
def download_only_video(link):
    global temp_status
    global file_size
    print(link)
    update_status("Checking link")
    if link!="":
        try:
            yt=YouTube(link,on_progress_callback=progress)
        except:
            update_status("Enter valid link")
            sleep(0.8)
            clear_url_box()
            update_status("Ready to download video")
            return

        if download_in_audio_format.get():
            update_status("Collecting information to download audio.")
            video = yt.streams.filter(only_audio=True).first()
            # print(video)
        else:
            update_status("Collecting information to download video.")
            video = yt.streams.filter(progressive=True,file_extension='mp4')
            video = video.get_highest_resolution()
        # print(video)

        try:
            # downloading the video
            file_size=video.filesize
            temp_status=f"Downloading video\nTitle:{video.title}\nSize:{video.filesize/1000000} MB"
            update_percentage_status(0)
            video.download(download_path.get())
        except:
            update_status("Some Error!")
            clear_url_box()
            return
            # print("Some Error!")
            # print('Task Completed!')
        update_status("Video Downloaded")
        delete_list()
        sleep(0.4)
        clear_url_box()
        update_status("Ready to download video")
    else:
        update_status("Enter valid link")
        sleep(0.4)
        clear_url_box()
        update_status("Ready to download video")
    


# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite Youtube Playlist Downloader")
    root.geometry("1000x650")
    root.minsize(1000,650)
    
    # Variables
    URL = StringVar()
    cur_path = StringVar()
    downloads_location=StringVar()
    statusvar = StringVar()
    download_in_audio_format = IntVar()
    download_path=StringVar()
    download_path.set(os.path.join(os.getcwd(),"Elite_youtube_downloader"))
    statusvar.set("Ready to download")
    # code to download a video
    heading1=Label(root,text="ELITE AKSHAY",font="calibre 40 bold",relief=RAISED,background="cyan",padx=10,pady=9)
    heading1.pack()
    space=Label(root,text="",font="calibre 2 bold")
    space.pack()
    heading2=Label(root,text="YOUTUBE DOWNLOADER",font="Times 25 bold",relief=RAISED,background="cyan",padx=10,pady=9,)
    heading2.pack()
    f1=Frame(root)
    f1.pack(side=TOP,fill=BOTH,expand=True,pady=10)
    name=Label(f1,text="ENTER URL OF PLAYLIST OR VIDEO",font="calibre 20 bold italic",relief=FLAT,padx=8,pady=3)
    name.pack()
    space=Label(f1,text="",font="calibre 2 bold")
    space.pack()
    url_input=Entry(f1,textvariable=URL,font="calibre 25 normal",relief=SUNKEN)
    url_input.pack()

    paste_url_btn=Button(f1,text="PASTE URL",command=paste_url,bd=5,font="calibre 18 bold")
    paste_url_btn.pack(side = LEFT, expand = True, fill = X)
    clear_url_btn=Button(f1,text="CLEAR URL",command=clear_url_box,bd=5,font="calibre 18 bold")
    clear_url_btn.pack(side = LEFT, expand = True, fill = X)
    Button(f1,text="Download Folder",command=select_folder,bd=5,font="calibre 18 bold").pack(side = LEFT, expand = True, fill = X)
    
    f4=Frame()
    f4.pack(side=TOP,fill=BOTH,expand=True)
    downloads_location.set(f"Downloads path :- {download_path.get()}")
    download_loacation_display=Label(f4,textvariable=downloads_location,font="calibre 10 bold italic",relief=FLAT,padx=8,pady=3)
    download_loacation_display.pack()

    Checkbutton(root,text="Download in audio format",variable=download_in_audio_format,font="calibre 14 bold",fg="red",onvalue=1,offvalue=0).pack(anchor='w')
    f2=Frame(root)
    f2.pack(side=TOP,fill=BOTH,expand=True)
    download_video_btn=Button(f2,text="Download Video",command=queue_only_video,bd=5,fg="blue",font="calibre 18 bold")
    download_video_btn.pack(side = LEFT, expand = True, fill = X)
    download_playlist_btn=Button(f2,text="Download Playlist",command=queue_playlist,bd=5,fg="blue",font="calibre 18 bold")
    download_playlist_btn.pack(side = LEFT, expand = True, fill = X)

    # show files 
    f3=Frame(root)
    f3.pack(side=TOP,fill=BOTH,expand=True)
    heading_files=Label(f3,text="Downloads",font="Times 20 bold",relief=RAISED,background="yellow",padx=10,pady=9,)
    heading_files.pack(side=TOP)
    # files 
    mylist = Listbox(f3,height=4)
    mylist.pack(side=LEFT,fill=BOTH,expand=True)
    Scroll =Scrollbar(f3)
    Scroll.pack(side=RIGHT,fill=Y)

    Scroll.config(command=mylist.yview)
    mylist.config(yscrollcommand=Scroll.set)


    
    
    # statusbar
    sbar = Label(root,textvariable=statusvar, relief=SUNKEN, anchor="w",padx=10,pady=7,background="cyan",fg="red",font="calibre 12 bold")
    sbar.pack(side=BOTTOM, fill=X)
    try:
        delete_list()
    except:
        os.mkdir(download_path.get())

    root.mainloop()