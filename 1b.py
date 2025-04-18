import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the filename if needed)
file_path = "Trips_by_Distance (1).csv"  # Update this if your file has a different name
travel_data = pd.read_csv(file_path)

# Optional: Fill or drop missing values
# travel_data = travel_data.fillna(travel_data.mean(numeric_only=True)).dropna()

# Filter rows where specific trip ranges exceed 10 million
short_range = travel_data[travel_data['Number of Trips 10-25'] > 10_000_000].copy()
medium_range = travel_data[travel_data['Number of Trips 50-100'] > 10_000_000].copy()

# Get the dates for each category
dates_short_range = short_range['Date']
dates_medium_range = medium_range['Date']

# Display how many dates match the filter
print(f"Days with over 10M trips (10-25 miles): {len(dates_short_range)}")
print(dates_short_range.head())

print(f"\nDays with over 10M trips (50-100 miles): {len(dates_medium_range)}")
print(dates_medium_range.head())

# Convert 'Date' to datetime objects
short_range['Date'] = pd.to_datetime(short_range['Date'])
medium_range['Date'] = pd.to_datetime(medium_range['Date'])

# ---- Visualization ----

plt.figure(figsize=(14, 6))

# Subplot 1: 10-25 mile range
plt.subplot(1, 2, 1)
plt.scatter(short_range['Date'], short_range['Number of Trips 10-25'], color='steelblue', alpha=0.6)
plt.title('Trips (10–25 miles) Above 10M')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(True)

# Subplot 2: 50–100 mile range
plt.subplot(1, 2, 2)
plt.scatter(medium_range['Date'], medium_range['Number of Trips 50-100'], color='seagreen', alpha=0.6)
plt.title('Trips (50–100 miles) Above 10M')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()