# Define the initial time
hours_start = 8
minutes_start = 52
seconds_start = 45

# Define the arrival time
hours_end = 12
minutes_end = 15
seconds_end = 10

# Convert the initial time to total seconds
total_seconds_start = hours_start * 3600 + minutes_start * 60 + seconds_start

# Convert the arrival time to total seconds
total_seconds_end = hours_end * 3600 + minutes_end * 60 + seconds_end

# Calculate the total travel time in seconds
total_travel_time_seconds = total_seconds_end - total_seconds_start

# Convert the total travel time to hours, minutes, and seconds
hours_travel = total_travel_time_seconds // 3600
minutes_travel = (total_travel_time_seconds % 3600) // 60
seconds_travel = total_travel_time_seconds % 60

# Print the result
print(f"Waktu yang dihabiskan dalam perjalanan adalah {hours_travel} jam, {minutes_travel} menit, dan {seconds_travel} detik.")