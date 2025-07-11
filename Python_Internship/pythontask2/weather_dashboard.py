import requests
import matplotlib.pyplot as plt
import datetime

def fetch_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def parse_weather_data(data):
    temps = []
    times = []
    for entry in data["list"]:
        temps.append(entry["main"]["temp"])
        time = datetime.datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
        times.append(time)
    return times, temps

def plot_temperature(times, temps, city_name):
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o', linestyle='-', color='b')
    plt.title(f"Temperature Forecast for {city_name}")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("temperature_plot.png")
    plt.show()

if __name__ == "__main__":
    city = "Chennai"
    api_key = "5a76a5929ebf4f10367060c620b35cbe"  
    print(f"Fetching weather data for {city}...")

    try:
        data = fetch_weather_data(city, api_key)
        if data.get("cod") != "200":
            print("Error fetching data:", data.get("message"))
        else:
            times, temps = parse_weather_data(data)
            plot_temperature(times, temps, city)
    except Exception as e:
        print("Failed to fetch or process weather data:", e)
