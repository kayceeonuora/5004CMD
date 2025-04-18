import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
travel_data = pd.read_csv("Trips_by_Distance (1).csv")
travel_data.fillna(travel_data.mean(numeric_only=True), inplace=True)

# Weekly trend of people staying at home
home_population_trend = travel_data.groupby('Week')['Population Staying at Home'].mean().reset_index()

# Define trip categories
trip_category_columns = [
    'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5', 
    'Number of Trips 5-10', 'Number of Trips 10-25', 'Number of Trips 25-50', 
    'Number of Trips 50-100', 'Number of Trips 100-250', 'Number of Trips 250-500', 
    'Number of Trips >=500'
]

# Set midpoints for calculating average travel distance
distance_categories = [0.5, 2, 4, 7.5, 17.5, 37.5, 75, 175, 375, 500]

# Calculate the total number of trips in each distance bracket
total_trip_counts = travel_data[trip_category_columns].sum()

# Calculate the number of travelers that are not staying at home
away_population = travel_data['Population Not Staying at Home'].sum()

# Estimate the average travel distance
estimated_avg_distance = (total_trip_counts * distance_categories).sum() / away_population

# Print outputs
print("📊 Weekly Home Population Trend:\n", home_population_trend)
print(f"📏 Estimated Average Travel Distance: {round(estimated_avg_distance, 2)} miles")

# --- Plot 1: Weekly Home Population Trend ---
plt.figure(figsize=(10, 5))
sns.lineplot(data=home_population_trend, x='Week', y='Population Staying at Home', marker="o", color='teal')
plt.title('Weekly Trend: Population Staying at Home')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("weekly_home_population_trend.png")
plt.show()

# --- Plot 2: Total Trips by Distance Category ---
plt.figure(figsize=(12, 6))
sns.barplot(x=total_trip_counts.index, y=total_trip_counts.values, color='darkorange')
plt.title('Total Number of Trips by Distance Category')
plt.xlabel('Distance Category')
plt.ylabel('Total Trips')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("total_trips_by_distance_category.png")
plt.show()