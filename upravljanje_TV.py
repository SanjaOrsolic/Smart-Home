from tkinter import*
import webview


root=Tk()
root.title("Smart TV")
root.geometry("800x510")
root.config(bg="#343a40")

sz_yt_slika=PhotoImage(file="Snimka zaslona YT.png")
sz_net_slika=PhotoImage(file="snimka_zaslona_netflix.png")
sz_hbo_slika=PhotoImage(file="snimka_zaslona_hbo.png")

naslov=Label(root,text="Smart TV", font=("Cavolini",20),bg="#343a40", fg="white")
naslov.place(x=20,y=20)

def yt_kanal():
    sz_yt_prikaz=Label(root, image=sz_yt_slika)
    sz_yt_prikaz.place(x=180,y=10)
def net_kanal():
    sz_net_prikaz=Label(root, image=sz_net_slika)
    sz_net_prikaz.place(x=180,y=10)
def hbo_kanal():
    sz_hbo_prikaz=Label(root, image=sz_hbo_slika)
    sz_hbo_prikaz.place(x=180,y=10)

jacina_vol=0
znak="| "
def povecanje_vol():
    global jacina_vol
    global znak
    if jacina_vol<=30:
        jacina_vol=jacina_vol+2
        volumen_text=Label(root,text=f"Volumen: {jacina_vol*znak}", font=("Cavolini",14),bg="#4472ca",fg="white")
        volumen_text.place(x=180, y=320)
    

def smanjenje_vol():
    volumen_text=Label(root,text="Volumen:                                                                           ", font=("Cavolini",14),bg="#343a40",fg="white")
    volumen_text.place(x=180, y=320)
    global jacina_vol
    global znak
    jacina_vol=jacina_vol-2 
    vol_text=Label(root,text=f"Volumen: {jacina_vol*znak}", font=("Cavolini",14),bg="#4472ca",fg="white")
    vol_text.place(x=180, y=320)
def iskljuci():
    off=Frame(root, bg="#343a40", width=610,height=310)
    off.place(x=180,y=10)

iskljuci_gumb=Button(root,text="Iskljuci TV", font=("Cavolini",14),bg="#212529",fg="white",width=12, command=iskljuci )
iskljuci_gumb.place(x=20,y=80)

volumen_text=Label(root,text="Volumen", font=("Cavolini",14),bg="#343a40", fg="white")
volumen_text.place(x=20,y=250)
povecaj_vol=Button(root,text="+", font=("Cavolini",14),bg="#212529",fg="white",width=5 ,command=povecanje_vol)
povecaj_vol.place(x=90,y=280)
smanji_vol=Button(root,text="-", font=("Cavolini",14),bg="#212529",fg="white",width=5, command=smanjenje_vol)
smanji_vol.place(x=20,y=280)


okvir_postavke=Frame(root, bg="#495057", width=800,height=150, relief=RAISED, )
okvir_postavke.place(x=0,y=350)

yt_slika=PhotoImage(file="YT_logo.png").subsample(2)
yt=Button(okvir_postavke, image=yt_slika, command=yt_kanal)
yt.place(x=60,y=10)

NeT_slika=PhotoImage(file="Netflix-logo.png").subsample(2)
NeT=Button(okvir_postavke, image=NeT_slika, command=net_kanal)
NeT.place(x=290,y=10)

HBO_slika=PhotoImage(file="HBO_logo.png").subsample(2)
HBO=Button(okvir_postavke, image=HBO_slika, command=hbo_kanal)
HBO.place(x=510,y=10)



root.mainloop()