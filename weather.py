import csv
import math

from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
    and Celcius symbols.
    
    Args:
    temp: A string representing a temperature.
    
    Returns:
    A string contain the temperature and "degrees Celcius."
    """    
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #convert ISO format date into datetime 
    dt = datetime.fromisoformat(iso_string)

    #convert the datetime into human-readable format
    human_readable_date = dt.strftime("%A %d %B %Y")

    return human_readable_date

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # Convert Fahrenheit to Celsius
    temp_in_celsius = (float(temp_in_fahrenheit) - 32)* 5 / 9
    temp =  float(temp_in_celsius)
    
    # Print and Round to 1 decimal place
    return round(temp, 1)
    

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    if not weather_data:
        raise ValueError("The list of weather_data is empty.")
    
    # Convert all items to floats
    weather_data = [float(item) for item in weather_data]
    
    mean_value = sum(weather_data) / len(weather_data)
    return float(mean_value)



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []

    #Open csv file
    with open(csv_file) as file:
        reader = csv.reader(file)
        header = next(reader)
        
        # Read the rest of the file
        for row in reader:
            if row:  # Only process non-empty rows
                # Convert the first two elements to integers if they are numeric
                try:
                    row[1] = int(row[1])
                except ValueError:
                    pass  # If conversion fails, keep the original value
                
                try:
                    row[2] = int(row[2])
                except ValueError:
                    pass  # If conversion fails, keep the original value
                
                data.append(row)
    
    return data
    

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return ()
    
    min_value = weather_data[0]
    min_index = 0
    
    for index, value in enumerate(weather_data):
        if value < min_value:
            min_value = value
            min_index = index
        elif value == min_value:
            min_index = index

    return float(min_value), min_index

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    
    max_value = weather_data[0]
    max_index = -1
    
    for index, value in enumerate(weather_data):
        if value > max_value:
            max_value = value
            max_index = index
        elif value == max_value:
            max_index = index

    return float(max_value), max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min_temps = []
    max_temps = []
    
        # Number of days of data
    num_days = len(weather_data)

    # Iterate through each day's data
    for day in weather_data:
        iso_string, low_temp_f, high_temp_f = day
        date = datetime.fromisoformat(iso_string)  # Parse the ISO 8601 date string

        # Convert temperatures from Fahrenheit to Celsius
        low_temp_c = (low_temp_f - 32) * 5.0 / 9.0
        high_temp_c = (high_temp_f - 32) * 5.0 / 9.0

        # Append temperatures and dates to lists
        min_temps.append((low_temp_c, date))
        max_temps.append((high_temp_c, date))

    # Find the lowest and highest temperatures and their dates
    min_temp, min_temp_date = min(min_temps, key=lambda x: x[0])
    max_temp, max_temp_date = max(max_temps, key=lambda x: x[0])

    # Calculate average temperatures
    average_low = sum(temp for temp, _ in min_temps) / len(min_temps)
    average_high = sum(temp for temp, _ in max_temps) / len(max_temps)
    
        # Adjust the overview label based on the number of days
    overview_label = f"{num_days} Day Overview"

    # Format the summary
    summary = (
        f"{overview_label}\n"
        # f"Overview\n"
        f"  The lowest temperature will be {min_temp:.1f}{DEGREE_SYMBOL}, and will occur on {min_temp_date.strftime('%A %d %B %Y')}.\n"
        f"  The highest temperature will be {max_temp:.1f}{DEGREE_SYMBOL}, and will occur on {max_temp_date.strftime('%A %d %B %Y')}.\n"
        f"  The average low this week is {average_low:.1f}{DEGREE_SYMBOL}.\n"
        f"  The average high this week is {average_high:.1f}{DEGREE_SYMBOL}.\n"
    )
    print('SUMMARY -->', summary)

    return (summary) 




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Initialize a list to store each day's summary
    daily_summaries = []

    # Iterate through each day's data
    for day in weather_data:
        iso_string, low_temp_f, high_temp_f = day
        date = datetime.fromisoformat(iso_string)  # Parse the ISO 8601 date string

        # Convert temperatures from Fahrenheit to Celsius
        low_temp_c = (low_temp_f - 32) * 5.0 / 9.0
        high_temp_c = (high_temp_f - 32) * 5.0 / 9.0

        # Create the summary for the day
        daily_summary = (
            f"---- {date.strftime('%A %d %B %Y')} ----\n"
            f"  Minimum Temperature: {low_temp_c:.1f}{DEGREE_SYMBOL}\n"
            f"  Maximum Temperature: {high_temp_c:.1f}{DEGREE_SYMBOL}"
        )
        daily_summaries.append(daily_summary)

    # Join all daily summaries into a single string, ensuring no extra newline at the end
    return "\n\n".join(daily_summaries) + "\n\n"