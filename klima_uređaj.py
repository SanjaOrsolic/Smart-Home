from tkinter import*

root=Tk()
root.title("Smart Home")
root.geometry("400x457")
root.config(bg="white")

okvir_naslov=Frame(root,bg="#cbf3f0", width=800, height=60,bd=3,relief=GROOVE)
okvir_naslov.place(x=0,y=0)
naslov_svijetlo=Label(okvir_naslov, text="Upravljanje klima uređajem", font=("Cavolini",20),bg="#cbf3f0")
naslov_svijetlo.place(x=30,y=10)

post_temp=Label(root,text="Zadana temperatura hlađenja", font=("Cavolini",16),bg="white")
post_temp.place(x=60,y=80)

okvir_naslov1=Frame(root,bg="#4472ca", width=200, height=150, bd=5,relief=GROOVE)
okvir_naslov1.place(x=100,y=120)

trenutna_temperatura=22

def povecanje_temp():
    global trenutna_temperatura
    trenutna_temperatura=trenutna_temperatura+1
    temp_text=Label(okvir_naslov1,text=f"{trenutna_temperatura} °C", font=("Cavolini",40),bg="#4472ca",fg="white")
    temp_text.place(x=30,y=30)

def smanjenje_temp():
    global trenutna_temperatura
    trenutna_temperatura=trenutna_temperatura-1
    temp_text=Label(okvir_naslov1,text=f"{trenutna_temperatura} °C", font=("Cavolini",40),bg="#4472ca",fg="white")
    temp_text.place(x=30,y=30)
jacina_fan=1
znak=") "
def povecanje_fan():
    global jacina_fan
    global znak
    if jacina_fan<=5:
        jacina_fan=jacina_fan+1
        temp_text=Label(okvir_naslov1,text=f"{jacina_fan*znak}", font=("Cavolini",14),bg="#4472ca",fg="white")
        temp_text.place(x=62, y=100)

def smanjenje_fan():
    fan_text=Label(okvir_naslov1,text="               ", font=("Cavolini",14),bg="#4472ca",fg="white")
    fan_text.place(x=62, y=100)
    global jacina_fan
    global znak
    jacina_fan=jacina_fan-1 
    fan_text=Label(okvir_naslov1,text=f"{jacina_fan*znak}", font=("Cavolini",14),bg="#4472ca",fg="white")
    fan_text.place(x=62, y=100)

temp_text=Label(okvir_naslov1,text=f"{trenutna_temperatura} °C", font=("Cavolini",40),bg="#4472ca",fg="white")
temp_text.place(x=30,y=30)
fan_text=Label(okvir_naslov1,text=f"Fan: {jacina_fan*znak} ", font=("Cavolini",14),bg="#4472ca", fg="white")
fan_text.place(x=20, y=100)

postavka_temp_text=Label(root,text="Postavke temperature:", font=("Cavolini",12),bg="white")
postavka_temp_text.place(x=20,y=280)

povecaj_temp=Button(root,text="+", font=("Cavolini",14),bg="#cbf3f0",width=5, command=povecanje_temp)
povecaj_temp.place(x=50,y=320)
smanji_temp=Button(root,text="-", font=("Cavolini",14),bg="#cbf3f0",width=5,command=smanjenje_temp)
smanji_temp.place(x=50,y=380)

postavka_fan_text=Label(root,text="Postavke jačine puhanja:", font=("Cavolini",12),bg="white")
postavka_fan_text.place(x=200,y=280)

povecaj_fan=Button(root,text="+", font=("Cavolini",14),bg="#cbf3f0",width=5, command=povecanje_fan)
povecaj_fan.place(x=250,y=320)
smanji_fan=Button(root,text="-", font=("Cavolini",14),bg="#cbf3f0",width=5,command=smanjenje_fan)
smanji_fan.place(x=250,y=380)




root.mainloop()