import requests

api_key = "75995229f1a20cedfc1959d7b463dd25"

city = input("Enter city name: ")
unit=input("choose unit(C/F):")
if unit.lower()=="f":
    units="imperial"
else:
    units="metric"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind=data["wind"]["speed"]

        print("\nWeather Details:")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)
        print(f"Wind speed:{wind} m/s")
        print("--------------------")
    else:
        print("City not found!")

except:
    print("Error fetching data. Check internet or API key.")