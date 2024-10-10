import requests
import matplotlib.pyplot as plt

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperatures = []
        
        for i in range(0, 40, 8):  
            day_temp = data['list'][i]['main']['temp']
            temperatures.append(day_temp)
        
        return temperatures
    else:
        print("Error fetching data:", response.status_code)
        return None

def calculate_average(temperatures):
    total = sum(temperatures)
    return total / len(temperatures)

def find_highest(temperatures):
    return max(temperatures)

def find_lowest(temperatures):
    return min(temperatures)

def present_results(average, highest, lowest):
    print("\nWeather Analysis Results:")
    print(f"Average Temperature: {average:.2f} °C")
    print(f"Highest Temperature: {highest} °C")
    print(f"Lowest Temperature: {lowest} °C")

def plot_temperatures_line_chart(temperatures):
    plt.figure(figsize=(10, 5))
    plt.plot(temperatures, marker='o', color='b')
    plt.title('Temperature Data Analysis')
    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.xticks(range(len(temperatures)), [f'Day {i+1}' for i in range(len(temperatures))])
    plt.grid(True)
    plt.show()

def main():
    api_key = "3e79b57fe1d68434c404a1f4df464c03" 
    city = input("Enter the city name for t weather forecast: ")
    
    temperatures = fetch_weather_data(city, api_key)
    
    if temperatures:
        average = calculate_average(temperatures)
        highest = find_highest(temperatures)
        lowest = find_lowest(temperatures)
        
        present_results(average, highest, lowest)
        plot_temperatures_line_chart(temperatures)

if __name__ == "__main__":
    main()