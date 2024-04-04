import requests

API_KEY = "d8af5788b98a09806111adfefff6fb95"  # Replace "your_api_key_here" with your actual OpenWeatherMap API key

def get_weather(location):
    """
    Function to fetch current weather data for a specified location using OpenWeatherMap API.
    :param location: Location (city name or ZIP code) for which to fetch weather data (string)
    :return: Dictionary containing weather data
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    print("Welcome to the Command-line Weather App!")
    location = input("Please enter the location (city name or ZIP code) for which you want to fetch weather data: ")

    weather_data = get_weather(location)
    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_conditions = weather_data["weather"][0]["description"]

        print(f"Current weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weather_conditions}")
    else:
        print(f"Error: Unable to fetch weather data. {weather_data['message']}")

if __name__ == "__main__":
    main()
