import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#TASK1 IN main.py
#Task2
# function to process weather data from the two files : 'data_temperature.txt' and 'Paris_data_climate.txt'
def process_weather_data(file1, file2):
    # function to load data from a given filename
    def load_data(filename, usecols=None):
        #specify data types for each column in the dataset
        dtype = [('Date', 'U10'), ('Location', 'U50'), ('Max_Temperature_C', 'f8'),
                 ('Min_Temperature_C', 'f8'), ('Precipitation_mm', 'f8'), ('Wind_Speed_kmh', 'f8'),
                 ('Humidity', 'f8'), ('Cloud_Cover', 'f8')] #U for Unicode string, 10 max length of the string #f for floats and 8 for 8 bytes that store the number
        return np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=dtype, usecols=usecols) #load the data from the file, specifying the delimiter, skipping the header, and using the defined data types

    data1 = load_data(file1) #load data from the first file
    data2 = load_data(file2, usecols=range(8)) #load data from the second file, using all 8 columns
    combined_data = np.concatenate((data1, data2)) #combine the data from the two files into a single dataset

    results = {} #initialize an empty dictionary to store the results
    for city in np.unique(combined_data['Location']): #loop through each unique city in the combined dataset
        city_data = combined_data[combined_data['Location'] == city] #filter the data to include only entries for the current city
        avg_temp = np.mean((city_data['Max_Temperature_C'] + city_data['Min_Temperature_C']) / 2) #calculate the average temperature for the city
        total_precip = np.sum(city_data['Precipitation_mm'])  #calculate the total precipitation for the city
        max_wind = np.max(city_data['Wind_Speed_kmh']) #find the maximum wind speed for the city
        min_wind = np.min(city_data['Wind_Speed_kmh']) #find the minimum wind speed for the city
        results[city] = { #store the calculated statistics in the results dictionary under the city name
            'Average Temperature': avg_temp,
            'Total Precipitation': total_precip,
            'Maximum Wind Speed': max_wind,
            'Minimum Wind Speed': min_wind
        }
    return results #return the compiled results

#TASK3

def read_data(file_name): #function to read data from a file
    with open(file_name, 'r') as file: #open the file for reading
        data = file.readlines()[1:]  #read all lines from the file, skipping the first line which is the header
    return data

def process_data(data): #function to process the read data
    dates, cities, max_temps = [], [], [] #initialize empty lists to store dates, city names, and maximum temperatures
    for line in data: #iterate over each line in the data
        parts = line.strip().split(',') #split the line into components
        dates.append(datetime.strptime(parts[0], '%Y-%m-%d'))  #convert the date string into a datetime object and add to the dates list
        cities.append(parts[1]) #adds the city name to the cities list
        max_temps.append(float(parts[2]))  #convert the temperature to float and append to the max_temps list
    return dates, cities, max_temps

def plot_temperature(dates, cities, max_temps): #function to plot the temperature over time for each city
    plt.figure(figsize=(15, 8)) #create a new figure for plotting with a specified size
    unique_cities = set(cities) #create a set of unique city names to avoid duplicates

    for city in unique_cities: #iterate over each unique city
        city_dates = [dates[i] for i in range(len(dates)) if cities[i] == city] #extract dates and temperatures for the current city
        city_temps = [max_temps[i] for i in range(len(dates)) if cities[i] == city]
        plt.plot(city_dates, city_temps, label=city) #plot the temperatures over time for the city

    plt.title('Max Temperature Over Time for Each City') #set the title and labels for the plot
    plt.xlabel('Date')
    plt.ylabel('Max Temperature (C)')
    plt.legend() # add a legend to the plot
    plt.grid(True) #enable grid for better readability
    plt.savefig("plottask3.png") #save the plot as an image file
    plt.show() #display the plot

def plot_average_temperature(cities, max_temps): #function to plot the average maximum temperature for different cities
    avg_temps = {city: 0 for city in set(cities)}  #initialize dictionaries to store the sum of temperatures and count for each city
    count = {city: 0 for city in set(cities)}

    for city, temp in zip(cities, max_temps): #accumulate total temperatures and count for each city
        avg_temps[city] += temp
        count[city] += 1

    for city in avg_temps: #calculate the average temperature for each city
        avg_temps[city] /= count[city]

    plt.figure(figsize=(10, 6)) #create a bar chart to display the average temperatures #initialize a new figure for plotting with a width of 10 inches and height of 6 inches
    plt.bar(avg_temps.keys(), avg_temps.values(), color='skyblue') #create a bar chart where the x-axis is city names and y-axis is their average temperatures, bars colored in sky blue
    plt.title('Average Max Temperature for Different Cities') #set the title of the chart to indicate what it represents
    plt.ylabel('Average Max Temperature (C)') #label the y-axis to show it represents average max temperatures in Celsius
    plt.xticks(rotation=45,fontsize=8) #rotate the labels on the x-axis (city names) by 45 degrees for better visibility and set the font size to 8
    plt.grid(axis='y') #enable grid lines along the y-axis to improve readability of the chart
    plt.savefig("barcharttask3.png") #save the generated bar chart as an image file named "barcharttask3.png"
    plt.show() #display the bar chart in a window


#TASK4

def categorize_temperature(day_record): #function to categorize a day based on its average temperature
    # Calculate the average temperature
    avg_temp = (day_record['Max Temperature (C)'] + day_record['Min Temperature (C)']) / 2 #calculate the average temperature for the day

    if avg_temp < 0: #determine the category of the day based on the average temperature
        return 'Cold' #if average temperature is below 0°C, categorize as 'Cold'
    elif 0 <= avg_temp < 15:
        return 'Moderate' #if average temperature is between 0°C and 15°C, categorize as 'Moderate'
    else:
        return 'Warm' #if average temperature is 15°C or above, categorize as 'Warm'

def hottest_and_coldest_days(data): #function to find the hottest and coldest days in the dataset
    hottest_day = max(data, key=lambda x: x['Max Temperature (C)']) #find the day with the highest maximum temperature
    coldest_day = min(data, key=lambda x: x['Min Temperature (C)'])  #find the day with the lowest minimum temperature
    return hottest_day, coldest_day  #return both the hottest and coldest day records

def overall_extreme_days(data): #function to find the overall extreme temperature days across all cities
    overall_hottest_day = max(data, key=lambda x: x['Max Temperature (C)']) #find the day with the absolute highest maximum temperature across all cities
    overall_coldest_day = min(data, key=lambda x: x['Min Temperature (C)']) #find the day with the absolute lowest minimum temperature across all cities
    return overall_hottest_day, overall_coldest_day #return both the overall hottest and coldest day records

def parse_data(file_path): #function to parse and process data from a file
    data = [] #initialize an empty list to store the data
    with open(file_path, 'r') as file:
        next(file)# Skip the header line
        for line in file:
            parts = line.strip().split(',') #split each line into parts
            #create a dictionary for each line with the appropriate data converted to float
            record = {
                'Date': parts[0],
                'Location': parts[1],
                'Max Temperature (C)': float(parts[2]),
                'Min Temperature (C)': float(parts[3]),
                'Precipitation (mm)': float(parts[4]),
                'Wind Speed (km/h)': float(parts[5]),
                'Humidity (%)': float(parts[6]),
                'Cloud Cover (%)': float(parts[7])
            }
            #if additional data for CO2 levels and sea level rise are present, add them to the record
            if len(parts) > 8:
                record['CO2 Levels (ppm)'] = float(parts[8])
                record['Sea Level Rise (mm)'] = float(parts[9])
            data.append(record) #add the processed record to the data list
    return data #return the list of processed data records

#TASK 5

def parse_climate_data(file_path): #function to analyse climate data from a file
    data = [] #initialize an empty list to store the parsed data
    with open(file_path, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            parts = line.strip().split(',')  #split each line into components
            record = { #create a dictionary for each line, converting date strings to datetime objects and other values to floats
                'Date': datetime.strptime(parts[0], '%Y-%m-%d'),
                'Max Temp': float(parts[2]),
                'Min Temp': float(parts[3]),
                'Precipitation': float(parts[4]),
                'CO2 Levels': float(parts[8]),
                'Sea Level Rise': float(parts[9])
            }
            data.append(record) #add the dictionary to the data list
    return data #return the list of dictionaries

def plot_relationship(dates, data1, label1, data2, label2, title, ylabel1, ylabel2): #function to plot the relationship between two sets of data
    fig, ax1 = plt.subplots(figsize=(12, 6)) #create a figure and a set of subplots
    # Plot the first set of data
    color = 'tab:red'
    ax1.set_xlabel('Date') #label the x-axis as 'Date'
    ax1.set_ylabel(ylabel1, color='#8B3FE2') #set the label for the left y-axis
    ax1.plot(dates, data1, color='#8B3FE2') #plot the first data set with a specific color
    ax1.tick_params(axis='y', labelcolor='#8B3FE2') #set the tick parameters for the left y-axis

    # Plot the second set of data
    ax2 = ax1.twinx() #create a second y-axis sharing the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel(ylabel2, color=color)  #set the label for the right y-axis
    ax2.plot(dates, data2, color=color) #plot the second data set with a different color
    ax2.tick_params(axis='y', labelcolor=color) #set the tick parameters for the right y-axis

    plt.savefig("sea_level_rise.png") #save the figure as an image file

    plt.title(title,color='#9999FF') #set the title of the plot with a specific color
    fig.tight_layout() #adjust the layout of the figure
    plt.savefig("CO2levelsgraph.png") #save the figure as an image file
    plt.show()  #display the plot

def calculate_correlation(data1, data2): #function to calculate the correlation between two datasets
    return np.corrcoef(data1, data2)[0, 1] #return the correlation coefficient between the two datasets


#Task 6

def display_city_weather(weather_data, city_name): #function to display weather statistics for a given city
    if city_name in weather_data:
        print(f"Weather statistics for {city_name}:") #print the city name
        for stat, value in weather_data[city_name].items(): #iterate through the statistics of the city and print them
            print(f"{stat}: {value}")
    else:
        print("Invalid city name or city not in dataset.") #print an error message if the city name is not in the dataset

#TASK 6 on the city_weather.py file to run