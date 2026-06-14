import requests

# API Key
API_KEY = "edfe25883b51ecb70137cfb17829d336"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data["cod"] == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        
        print("\n" + "=" * 45)
        print(f"  🌍 {city_name}, {country}")
        print("=" * 45)
        print(f"  🌡️  Temperature  : {temp}°C")
        print(f"  🤔 Feels Like   : {feels_like}°C")
        print(f"  💧 Humidity     : {humidity}%")
        print(f"  🌤️  Weather      : {weather.capitalize()}")
        print(f"  💨 Wind Speed   : {wind_speed} m/s")
        print("=" * 45)
    
    elif data["cod"] == 401:
        print("❌ API key sahi nahi — 2-3 ghante wait karo!")
    
    elif data["cod"] == "404":
        print("❌ City nahi mili! Sahi naam likho.")
    
    else:
        print(f"❌ Error: {data['message']}")

def weather_app():
    print("=" * 45)
    print("   🌤️  Weather App!")
    print("=" * 45)
    
    while True:
        print("\n1. City ka weather dekho")
        print("2. Exit")
        
        choice = input("\nOption choose karo (1/2): ")
        
        if choice == "1":
            city = input("City ka naam likho: ")
            get_weather(city)
        elif choice == "2":
            print("Bye! 👋")
            break
        else:
            print("❌ Galat option!")

weather_app()