import requests
import matplotlib.pyplot as plt

# -----------------------
# CONFIGURATION
# -----------------------
API_KEY = "b00648094c186297efdd1448e0f0d56a"    # Replace with your OpenWeatherMap API key
CITY = "Sawantwadi"

# -----------------------
# FETCH DATA FROM API
# -----------------------
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code != 200:
    print("Error fetching data:", response.text)
    exit()

data = response.json()

# Extract temperature vs time
times = []
temperatures = []

for entry in data['list']:
    times.append(entry['dt_txt'])
    temperatures.append(entry['main']['temp'])

# -----------------------
# VISUALIZATION
# -----------------------
plt.figure(figsize=(12,6))
plt.plot(times, temperatures, marker='o')
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Forecast for {CITY}")
plt.grid(True)
plt.tight_layout()
plt.show()