import requests
import matplotlib.pyplot as plt

API_KEY = "fd7fc4f57dd9bdf37b8d45c4376680f1"

cities = ["Mumbai", "Delhi", "Bengaluru"]
city_data = {}

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != "200":
        print(f"Error for {city}: ", data)
        continue

    dates, temps, humidity, wind = [], [], [], []

    for item in data["list"][:8]:
        dates.append(item["dt_txt"])
        temps.append(item["main"]["temp"])
        humidity.append(item["main"]["humidity"])
        wind.append(item["wind"]["speed"])

    city_data[city] = {
        "dates": dates,
        "temps": temps,
        "humidity": humidity,
        "wind": wind
    }

plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
for city in city_data:
    plt.plot(city_data[city]["dates"], city_data[city]["temps"], label=city)
plt.title("Temperature Comparison")
plt.ylabel("°C")
plt.legend()

plt.subplot(3, 1, 2)
for city in city_data:
    plt.plot(city_data[city]["dates"], city_data[city]["humidity"], label=city)
plt.title("Humidity Comparison")
plt.ylabel("%")
plt.legend()

plt.subplot(3, 1, 3)
for city in city_data:
    plt.plot(city_data[city]["dates"], city_data[city]["wind"], label=city)
plt.title("Wind Speed Comparison")
plt.ylabel("m/s")
plt.xlabel("Time")
plt.legend()

plt.tight_layout()
plt.show()
