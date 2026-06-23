# Weather API Project
# Developed by Deepitha R

import requests

# Get city name from user
city = input("Enter city name: ")

# Your API key
api_key = "06a5e9ad53554c48a21151138262306"

# API URL
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if city exists
if "error" in data:
    print("\n❌ City not found")
else:
    # Extract data
    city_name = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    wind_speed = data["current"]["wind_kph"]

    # Display weather report
    print("\n🌤 Weather Report")
    print("------------------------")
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Condition:", condition)
    print("Wind Speed:", wind_speed, "km/h")
