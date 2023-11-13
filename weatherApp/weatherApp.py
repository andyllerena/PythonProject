import requests
import json

def fetch_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "imperial",
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to fetch weather data. Status Code: {response.status_code}")
        print(response.text)  # Print the response content for debugging.
        return None

def display_weather_info(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°F")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Pressure: {weather_data['main']['pressure']} hPa")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("No weather data to display.")

if __name__ == "__main__":
    api_key = "d5c827900ade9aacafaf838bfe8494c6"  # Replace with your API key
    city_name = input("Enter a city name: ")

    weather_data = fetch_weather_data(api_key, city_name)

    if weather_data:
        display_weather_info(weather_data)











