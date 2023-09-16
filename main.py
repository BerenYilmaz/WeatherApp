import tkinter as tk
import requests
import time

def getWeather(window):
    api_key = "9d0c2ef63464655ff932fe12137162e9"
    city = entry_1.get()
    api = ("https://api.openweathermap.org/data/2.5/weather?q=" + city +
           "&appid=9d0c2ef63464655ff932fe12137162e9"
           )
    json_data = requests.get(api).json()
    temp = int(json_data['main']['temp'] - 273.15)
    condition = json_data['weather'][0]['main']
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = ("\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " +
                  str(pressure) +  "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" +
                  "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
                  )
    label_1.config(text= final_info)
    label_2.config(text= final_data)

window = tk.Tk()
window.geometry("600x500")
window.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

entry_1 = tk.Entry(window, font= t)
entry_1.pack(pady = 20)
entry_1.focus()
entry_1.bind('<Return>', getWeather)


label_1 = tk.Label(window, font = t)
label_1.pack()
label_2 = tk.Label(window, font = f)
label_2.pack()

window.mainloop()