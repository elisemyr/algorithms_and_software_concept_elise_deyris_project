from code import process_weather_data
import sys
import code

# Paths to your data files TASK1
file1 = 'data_temperature.txt'
file2 = 'Paris_data_climate.txt'

#TASK2

weather_stats = process_weather_data(file1, file2) #process the weather data from both files and store the results

#loop through the processed data and print the weather statistics for each city
for city, stats in weather_stats.items():
    print(f"City: {city}") #print the city name
    for stat, value in stats.items():
        print(f"{stat}: {value}") #print each statistic and its value for the city
    print("\n") #newline

#TASK3

import code

data1 = code.read_data('data_temperature.txt') #read and process weather data for temperature analysis for the first file
data2 = code.read_data('Paris_data_climate.txt') #read and process weather data for temperature analysis for the second file

#process the read data to extract dates, cities, and maximum temperatures
dates1, cities1, max_temps1 = code.process_data(data1)
dates2, cities2, max_temps2 = code.process_data(data2)

#combine the data from both sources
dates = dates1 + dates2
cities = cities1 + cities2
max_temps = max_temps1 + max_temps2

code.plot_temperature(dates, cities, max_temps) #plot the temperature data using functions from the code module
code.plot_average_temperature(cities, max_temps)

#TASK4
import code

#file paths for the dataset text files
file_path1 = 'data_temperature.txt'
file_path2 = 'Paris_data_climate.txt'

#parse the data from both files
data1 = code.parse_data(file_path1)
data2 = code.parse_data(file_path2)

#combine the datasets
combined_data = data1 + data2

#analyze the combined data for each city
for city in set(record['Location'] for record in combined_data):
    city_data = [record for record in combined_data if record['Location'] == city]
    for day_record in city_data: #categorize temperature and find extreme temperature days for each city
        day_record['Temperature Category'] = code.categorize_temperature(day_record)

    #find the hottest and coldest day for the city
    hottest_day, coldest_day = code.hottest_and_coldest_days(city_data)
    print(f'{city} - Hottest day: {hottest_day}, Coldest day: {coldest_day}')

#find the overall hottest and coldest day across all cities
overall_hottest, overall_coldest = code.overall_extreme_days(combined_data)
print(f'Overall hottest day: {overall_hottest}')
print(f'Overall coldest day: {overall_coldest}')

#TASK 5

import code

data_file = 'Paris_data_climate.txt'

#parse the climate data
data = code.parse_climate_data(data_file)

#extract relevant data for analysis and visualization
dates = [record['Date'] for record in data]
max_temps = [record['Max Temp'] for record in data]
min_temps = [record['Min Temp'] for record in data]
avg_temps = [(m + n) / 2 for m, n in zip(max_temps, min_temps)]
precipitations = [record['Precipitation'] for record in data]
co2_levels = [record['CO2 Levels'] for record in data]
sea_levels = [record['Sea Level Rise'] for record in data]

#visualize the relationships between temperature and other climate factors
code.plot_relationship(dates, avg_temps, 'Average Temperature (C)', co2_levels, 'CO2 Levels (ppm)',
                     'Temperature vs CO2 Levels', 'Temperature (C)', 'CO2 Levels (ppm)')

#visualize the relationship between temperature and sea level rise
code.plot_relationship(dates, avg_temps, 'Average Temperature (C)', sea_levels, 'Sea Level Rise (mm)',
                     'Temperature vs Sea Level Rise', 'Temperature (C)', 'Sea Level Rise (mm)')

#calculate and display the correlation between temperature and climate factors
temp_co2_corr = code.calculate_correlation(avg_temps, co2_levels)
temp_sea_level_corr = code.calculate_correlation(avg_temps, sea_levels)
print(f'Correlation between temperature and CO2 levels: {temp_co2_corr}')
print(f'Correlation between temperature and sea level rise: {temp_sea_level_corr}')

#TASK 6 on the city_weather.py file
