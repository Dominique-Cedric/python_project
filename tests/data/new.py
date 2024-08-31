


def generate_summary(weather_data):
    if not weather_data:
        return "No data available."

    # Initialize lists to hold all min and max temperatures
    min_temps = []
    max_temps = []
    min_dates = []
    max_dates = []

    # Iterate over the weather data to extract min and max temperatures
    for day_data in weather_data:
        if len(day_data) < 3:
            continue  # Skip invalid rows

        date, min_temp, max_temp = day_data
        try:
            min_temp = float(min_temp)
            max_temp = float(max_temp)
        except ValueError:
            continue  # Skip rows with invalid temperature values

        min_temps.append(min_temp)
        max_temps.append(max_temp)
        min_dates.append(date)  # Assuming date is in a recognizable format
        max_dates.append(date)

    if not min_temps or not max_temps:
        return "No valid temperature data available."

    # Calculate statistics
    overall_min = min(min_temps)
    overall_max = max(max_temps)
    average_min = sum(min_temps) / len(min_temps)
    average_max = sum(max_temps) / len(max_temps)

    # Find dates for min and max temperatures
    min_temp_date = min_dates[min_temps.index(overall_min)]
    max_temp_date = max_dates[max_temps.index(overall_max)]

    # Format the summary string to match the expected format
    summary = (
        f"8 Day Overview\n"
        f"  The lowest temperature will be {overall_min:.1f}°C, and will occur on {min_temp_date}.\n"
        f"  The highest temperature will be {overall_max:.1f}°C, and will occur on {max_temp_date}.\n"
        f"  The average low this week is {average_min:.1f}°C.\n"
        f"  The average high this week is {average_max:.1f}°C."
    )

    return summary