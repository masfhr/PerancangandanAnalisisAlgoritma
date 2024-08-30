# Define the initial time
hours = 8
minutes = 52
seconds = 45

# Convert the initial time to total seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

# Add 5000 seconds to the total seconds
total_seconds += 5000

# Convert the total seconds back to hours, minutes, and seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Print the result
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")