import requests
import json
while True:

    print("!! Welcome to the real time weather app !!")
    city = input("Enter the city name  : ")
    url = f"https://api.weatherapi.com/v1/current.json?key=7c246715f1a0443c92370902230604&q={city}"
    r=requests.get(url)
    # print(r.text)
    wdic = json.loads(r.text)
    print(wdic["current"]["temp_c"],"°C")