import requests

city = input("City/Country: ")

api_key = "your api"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
res = requests.get(url)

jsonfile = res.json()
try:
    kelvin = jsonfile["main"]["temp"]
    cond = jsonfile["weather"][0]["main"]
    place = jsonfile["name"]

    celsius = kelvin -  273.15
    celsius = round(celsius,2)


    currently = {"place":place,"temperature":celsius,"condition":cond}

    print(currently)

except Exception as e:

    print("An Error Has Occurred:\nPlease double-check that your 'City/Country:' exists\nTroubleshoot to (mail) if something is wrong")



