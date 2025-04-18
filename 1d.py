import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("cleaned_trips.csv")

# Print column names to debug
print("Columns in the dataset:", data.columns)

# Strip spaces from column names (if necessary)
data.columns = data.columns.str.strip()

# Define trip length categories (from shortest to longest)
categories = [
    'Trips <1',
    'Trips 1-3',
    'Trips 3-5',
    'Trips 5-10',
    'Trips 10-25',
    'Trips 25-50',
    'Trips 50-100',
    'Trips 100-250',
    'Trips 250-500',
    'Trips >=500'
]

# Check if the category names exist in the dataset
missing_columns = [col for col in categories if col not in data.columns]
if missing_columns:
    print(f"Warning: The following categories are missing from the data: {missing_columns}")
else:
    # Compute the total number of trips in each category
    category_totals = data[categories].sum()

    # Create the bar plot to visualize the data
    plt.figure(figsize=(12, 6))
    category_totals.plot(kind='bar', color='lightgreen')
    plt.title("Travel Frequency Distribution by Trip Length")
    plt.ylabel("Total Number of Trips")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig("trip_frequency_distribution.png")

    # Display the plot
    plt.show()