import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer



root_gl = Tk()
root_gl.title("Music Player")
root_gl.geometry("500x457")
root_gl.configure(bg="white")
root_gl.resizable(False, False)
mixer.init()

okvir_naslov=Frame(root_gl,bg="#cbf3f0", width=800, height=60)
okvir_naslov.place(x=0,y=0)
naslov_svijetlo=Label(okvir_naslov, text="Upravljanje glazbom", font=("Cavolini",20),bg="#cbf3f0")
naslov_svijetlo.place(x=140,y=10)


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

# Button
ButtonPlay = PhotoImage(file="play.png",master=root_gl)
Button(root_gl, image=ButtonPlay, bg="white", bd=0,
       command=PlayMusic).place(x=130, y=300)
ButtonStop = PhotoImage(file="stop.png",master=root_gl)
Button(root_gl, image=ButtonStop, bg="white", bd=0,
       command=mixer.music.stop).place(x=20, y=300)
ButtonResume = PhotoImage(file="resume.png",master=root_gl)
Button(root_gl, image=ButtonResume, bg="white", bd=0,
       command=mixer.music.unpause).place(x=240, y=300)
ButtonPause = PhotoImage(file="pause.png",master=root_gl)
Button(root_gl, image=ButtonPause, bg="white", bd=0,
       command=mixer.music.pause).place(x=350, y=300)
stop=Label(root_gl,text="Stop", font=("Cavolini",16),bg="white")
stop.place(x=50,y=400)
play=Label(root_gl,text="Play", font=("Cavolini",16),bg="white")
play.place(x=160,y=400)
resume=Label(root_gl,text="Resume", font=("Cavolini",16),bg="white")
resume.place(x=260,y=400)
pause=Label(root_gl,text="Pause", font=("Cavolini",16),bg="white")
pause.place(x=370,y=400)


Frame_Music = Frame(root_gl, bd=2, relief=RIDGE)
Frame_Music.place(x=20, y=140, width=450, height=150)
Button(root_gl, text="Open Folder", width=15, height=2, font=("Cavolini",
              12, "bold"), fg="Black", bg="#2ec4b6", command=AddMusic).place(x=20, y=80)
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=200, font=("Cavolini", 10), bg="#cbf3f0", fg="black", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

      
root_gl.mainloop()