import dask.dataframe as dd
import time

# Load the dataset
trip_data = dd.read_csv("Trips_Full Data (2).csv", assume_missing=True)

# Clean column names
trip_data.columns = trip_data.columns.str.strip()

# Check if 'Week of Date' exists
print(trip_data.columns)

# Simple analysis without using distributed client
start_time_1 = time.time()
avg_trips_1 = trip_data.groupby("Week of Date")["Trips 1-25 Miles"].mean().compute()
elapsed_1 = round(time.time() - start_time_1, 2)

start_time_2 = time.time()
avg_trips_2 = trip_data.groupby("Week of Date")["Trips 1-25 Miles"].mean().compute()
elapsed_2 = round(time.time() - start_time_2, 2)

print(f"Time for first run: {elapsed_1} sec")
print(f"Time for second run: {elapsed_2} sec")