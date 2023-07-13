import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

window = Tk()
window.title("Simpli Music Player")
window.geometry("485x700+290+10")
window.configure(background='#333333')
window.resizable(False, False)
mixer.init()


def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    
    
lower_frame = Frame(window , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)



image_icon = PhotoImage(file="logo png.png")
window.iconphoto(False, image_icon)


frameCnt = 30
frames = [PhotoImage(file='imageee.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(40, update, ind)
label = Label(window)
label.place(x=0, y=0)
window.after(0, update, 0)

ButtonPlay = PhotoImage(file="play.png")
Button(window, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=215, y=487)

ButtonStop = PhotoImage(file="stop.png")
Button(window, image=ButtonStop, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.stop).place(x=130, y=487)

Buttonvolume = PhotoImage(file="volume.png")
Button(window, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=20, y=487)

ButtonPause = PhotoImage(file="pause.png")
Button(window, image=ButtonPause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.pause).place(x=300, y=487)
    
Menu = PhotoImage(file="menu.png")
Label(window, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(window, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

Button(window, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

window.mainloop()