
import sys
import code

def main():
    file1 = 'data_temperature.txt' #paths to the data files
    file2 = 'Paris_data_climate.txt'
    weather_stats = code.process_weather_data(file1, file2) #process the weather data using a function from the code module

    if len(sys.argv) > 1: #check if a city name is provided as a command-line argument
        city_name = sys.argv[1] #store the city name from the command-line argument
        code.display_city_weather(weather_stats, city_name) #display the weather statistics for the specified city using a function from the 'code' module
    else:
        print("City name not provided. Usage: python3 city_weather.py [City Name]") #print a message indicating how to use the script if no city name is provided

if __name__ == "__main__":
    main()
