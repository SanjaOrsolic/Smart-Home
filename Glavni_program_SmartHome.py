from tkinter import*
import os
from prognoza_vremena import*



root=Tk()
root.title("Smart Home")
root.geometry("800x457")
root.config(bg="white")

slika_bg=PhotoImage(file="house.png")
video_slika=PhotoImage(file="kameraa.png").subsample(3)
svjetlo_slika=PhotoImage(file="light.png").subsample(3)
termo_slika=PhotoImage(file="termometar.png").subsample(3)
tv_slika=PhotoImage(file="tv.png").subsample(3)
glazba_slika=PhotoImage(file="music.png").subsample(3)
vrijeme_slika=PhotoImage(file="vrijeme.png").subsample(3)

pozadina=Label(root,image=slika_bg)
pozadina.place(x=0,y=0)

def svjetlo():
    root2=Toplevel()
    root2.title("Svjetlo")
    root2.geometry("800x457")
    root2.config(bg="white")

    def mrak_dnevna():
        dnevna_mrak_slika=PhotoImage(file="dneva_mrak.png",master=root)
        dnevna_mrak=Label(root2,image=dnevna_mrak_slika)
        dnevna_mrak.place(x=10,y=80)
        root2.mainloop()
    def svjetlo_dnevna():
        dnevna=Label(root2,image=dnevna_slika)
        dnevna.place(x=10,y=80)
        root2.mainloop()
    def mrak_kuhinja():
        kuhinja_mrak_slika=PhotoImage(file="kuhinja_mrak.png",master=root)
        kuhinja_mrak=Label(root2,image=kuhinja_mrak_slika)
        kuhinja_mrak.place(x=270,y=80)
        root2.mainloop()
    def svjetlo_kuhinja():
        kuhinja=Label(root2,image=kuhinja_slika)
        kuhinja.place(x=270,y=80)
        root2.mainloop()
    def mrak_soba():
        soba_mrak_slika=PhotoImage(file="soba_mrak.png",master=root)
        soba_mrak=Label(root2,image=soba_mrak_slika)
        soba_mrak.place(x=530,y=80)
        root2.mainloop()
    def svjetlo_soba():
        soba=Label(root2,image=soba_slika)
        soba.place(x=530,y=80)
        root2.mainloop()

    okvir_naslov=Frame(root2,bg="#cbf3f0", width=800, height=60)
    okvir_naslov.place(x=0,y=0)
    naslov_svijetlo=Label(okvir_naslov, text="Upravljanje svjetlom", font=("Cavolini",20),bg="#cbf3f0")
    naslov_svijetlo.place(x=290,y=10)

    dnevna_slika=PhotoImage(file="dneva.png",master=root)
    dnevna=Label(root2,image=dnevna_slika)
    dnevna.place(x=10,y=80)

    
    kuhinja_slika=PhotoImage(file="kuhinja.png",master=root)
    kuhinja=Label(root2,image=kuhinja_slika)
    kuhinja.place(x=270,y=80)

    soba_slika=PhotoImage(file="soba.png",master=root)
    soba=Label(root2,image=soba_slika)
    soba.place(x=530,y=80)

    ukljuci_dnevna=Button(root2,text="Ukljuci svjetlo", font=("Cavolini",14),bg="#f0ead2",width=15, command=svjetlo_dnevna)
    ukljuci_dnevna.place(x=50,y=300)
    iskljuci_dnevna=Button(root2,text="Iskljuci svjetlo", font=("Cavolini",14),bg="#f0ead2",width=15,command=mrak_dnevna)
    iskljuci_dnevna.place(x=50,y=350)

    ukljuci_kuhinja=Button(root2,text="Ukljuci svjetlo", font=("Cavolini",14),bg="#f0ead2",width=15,command=svjetlo_kuhinja)
    ukljuci_kuhinja.place(x=320,y=300)
    iskljuci_kuhinja=Button(root2,text="Iskljuci svjetlo", font=("Cavolini",14),bg="#f0ead2",width=15,command=mrak_kuhinja)
    iskljuci_kuhinja.place(x=320,y=350)

    ukljuci_soba=Button(root2,text="Ukljuci svjetlo", font=("Cavolini",14),bg="#f0ead2",width=15, command=svjetlo_soba)
    ukljuci_soba.place(x=590,y=300)
    iskljuci_soba=Button(root2,text="Iskljuci svjetlo", font=("Cavolini",14),bg="#f0ead2",width=15,command=mrak_soba)
    iskljuci_soba.place(x=590,y=350)

    root2.mainloop()
def glazba():
    os.system("python pusti_glazbu.py")
def upravljanje_tv():
    os.system("python upravljanje_TV.py")

def upravljanje_termometrom():
    os.system("python klima_uređaj.py")


def videonadzor():
    root1=Toplevel()
    root1.title("Video nadzor")
    root1.geometry("800x457")
    root1.config(bg="white")

    okvir_naslov=Frame(root1,bg="#cbf3f0", width=800, height=60)
    okvir_naslov.place(x=0,y=0)
    naslov_video=Label(okvir_naslov, text="Video nadzor kuće", font=("Cavolini",20),bg="#cbf3f0")
    naslov_video.place(x=290,y=10)
    sec_camera_slika=PhotoImage(file="sec_camera.png",master=root)
    video=Label(root1,image=sec_camera_slika)
    video.place(x=80,y=80)
    root1.mainloop()    

def prikaz_ikona():

    video_icon=Button(root,image=video_slika, bd=1,command=videonadzor)
    video_icon.place(x=20,y=80)
    
    svjetlo_icon=Button(root,image=svjetlo_slika, bd=1,command=svjetlo)
    svjetlo_icon.place(x=20,y=200)
    
    termo_icon=Button(root,image=termo_slika, bd=1,command=upravljanje_termometrom)
    termo_icon.place(x=700,y=80)
   
    tv_icon=Button(root,image=tv_slika, bd=1, command=upravljanje_tv)
    tv_icon.place(x=20,y=320)
    
    glazba_icon=Button(root,image=glazba_slika, bd=1,command=glazba)
    glazba_icon.place(x=700,y=200)
    
    vrijeme_icon=Button(root,image=vrijeme_slika, bd=1, command=vremenska_prognoza)
    vrijeme_icon.place(x=700,y=320)

okvir_naslov=Frame(root,bg="#cbf3f0", width=800, height=60)
okvir_naslov.place(x=0,y=0)

naslov=Label(okvir_naslov, text="Smart Home", font=("Cavolini",20),bg="#cbf3f0")
naslov.place(x=320,y=10)

paljenje_slika=PhotoImage(file="power.png").subsample(4)
paljenje=Button(root,image=paljenje_slika,bd=0,command=prikaz_ikona)
paljenje.place(x=370,y=70)

root.mainloop()