from tkinter import*
import datetime as dt
import locale
import requests
import json

def vremenska_prognoza():

    def get_weather_data(api_key, city_id):  
        api_url = "http://api.openweathermap.org/data/2.5/weather"  
        params = {  
            "id": city_id,  
            "units": "metric",  
            "appid": api_key  
        }  
        response = requests.get(api_url, params=params)  
        data = response.json()  
        return data  
    
    api_key = "c94a2499bf7fc730cc0e2d7777112526"  
    city_id = "3186294"  # Žu 
    
    podaci = get_weather_data(api_key, city_id)  

    
    temperature = podaci["main"]["temp"]  
    city = podaci["name"]  
    humidity = podaci["main"]["humidity"]  
    wind_speed = podaci["wind"]["speed"]
    vrijeme_ikona=podaci['weather'][0]['description']
    
    import time  
    import threading  
    
    def get_hourly_weather_data():  
        while True:  
            data = get_weather_data(api_key, city_id)  
            time.sleep(3600) 
    
    thread = threading.Thread(target=get_hourly_weather_data)  
    thread.start()


    filename_json = 'weather_Zu.json'
    with open(filename_json, 'w') as file:
        json.dump(podaci, file, indent=4)


    root_v=Toplevel()
    root_v.geometry("800x300")
    root_v.title("Vremenska prognoza")
    root_v.config(bg="white")
    root_v.resizable(False,False)

    okvir_naslov=Frame(root_v,bg="#cbf3f0", width=800, height=60)
    okvir_naslov.place(x=0,y=0)
    naslov_vrijeme=Label(okvir_naslov, text="Vremenska prognoza", font=("Cavolini",20),bg="#cbf3f0")
    naslov_vrijeme.place(x=290,y=10)


    #-----Datum i vrijeme
    locale.setlocale(locale.LC_TIME, 'hr_HR')
    datum=dt.datetime.now()
    lijepi_datum=datum.strftime("%d. %B %Y.")
    dan=datum.strftime("%A")
    dan_prikaz=dan.capitalize()

    def vrijeme():
        sat=time.strftime("%H:%M:%S")
        sat_prikaz=Label(root_v, text=sat, font=("Comic Sans MS", 24), bg="white",padx=10)
        sat_prikaz.place(x=50, y=160)
        root_v.after(1000,vrijeme)
    vrijeme()

    #-----Datum i vrijeme GUI
    datum_prikaz=Label(root_v, text=(f"{dan_prikaz},  {lijepi_datum}"), font=("Comic Sans MS", 14), bg="white")
    datum_prikaz.place(x=20,y=100)



    #----- Temperatura i vrijeme GUI
    grad=Label(root_v, text=f"{city} ",font=("Comic Sans MS", 16), bg="white")
    grad.place(x=450,y=80)
    temp_text=Label(root_v,text="Temperatura:",font=("Comic Sans MS", 12), bg="white")
    temp_text.place(x=580,y=90)
    temp_prikaz=Label(root_v,text=f"{round(temperature)} °C",font=("Comic Sans MS", 18), bg="white")
    temp_prikaz.place(x=610,y=115)
    tlak_zraka_text=Label(root_v,text="Brzina vjetra:",font=("Comic Sans MS", 12), bg="white")
    tlak_zraka_text.place(x=580,y=150)
    brzina_vjetra_prikaz=Label(root_v,text=f"{round(wind_speed,1)} m/s",font=("Comic Sans MS", 14), bg="white")
    brzina_vjetra_prikaz.place(x=610,y=175)
    vlaznost_text=Label(root_v,text="Vlaznost:",font=("Comic Sans MS", 12), bg="white")
    vlaznost_text.place(x=610,y=210)
    vlaznost_prikaz=Label(root_v,text=f"{round(humidity)} %",font=("Comic Sans MS", 14), bg="white")
    vlaznost_prikaz.place(x=630,y=235)

       
    
    if vrijeme_ikona=="broken clouds" or vrijeme_ikona=="overcast clouds":
        clouds=PhotoImage(file="clouds.png").subsample(4)
        clouds_prikaz=Label(root_v, image=clouds,bg="white")
        clouds_prikaz.place(x=430,y=120)
    elif vrijeme_ikona=="moderate rain" or vrijeme_ikona=="light rain" or vrijeme_ikona=="heavy intensity rain":
        rain=PhotoImage(file="rain.png").subsample(4)
        rain_prikaz=Label(root_v, image=rain,bg="white")
        rain_prikaz.place(x=430,y=120)
    elif vrijeme_ikona=="few clouds" or vrijeme_ikona=="scattered clouds":
        few_clouds=PhotoImage(file="few_clouds.png").subsample(30)
        few_clouds_prikaz=Label(root_v, image=few_clouds,bg="white")
        few_clouds_prikaz.place(x=430,y=120)
    elif vrijeme_ikona=="clear sky":
        clear_sky=PhotoImage(file="clear_sky.png").subsample(3)
        clear_sky_prikaz=Label(root_v, image=clear_sky,bg="white")
        clear_sky_prikaz.place(x=400,y=120)
    
    else:
        pass
   

    root_v.mainloop()