# --------------------------------------------
# Weather Data Visualizer – Mini Project (Simple Version)
# --------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Task 1: Load the Dataset
# -------------------------------

df = pd.read_csv("data.csv")   # load 30-days data

print("\n--- DATA HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())

# -------------------------------
# Task 2: Data Cleaning
# -------------------------------

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])  # remove wrong dates

# fill missing values (if any)
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
df['rainfall'] = df['rainfall'].fillna(0)

# -------------------------------
# Task 3: Statistics
# -------------------------------

print("\n--- TEMPERATURE STATS ---")
print("Mean:", df['temperature'].mean())
print("Max :", df['temperature'].max())
print("Min :", df['temperature'].min())
print("Std :", np.std(df['temperature']))

# Monthly grouping
df['month'] = df['date'].dt.month
monthly = df.groupby('month')[['temperature','rainfall','humidity']].mean()

print("\n--- MONTHLY AVERAGE ---")
print(monthly)

# -------------------------------
# Task 4: Plots
# -------------------------------

# Daily temp line plot
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("daily_temperature.png")
plt.show()

# Monthly rainfall bar chart
plt.bar(monthly.index, monthly['rainfall'])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.savefig("monthly_rainfall.png")
plt.show()

# Humidity vs Temp scatter
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("humidity_vs_temp.png")
plt.show()

# Combined plots
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(df['date'], df['temperature'])
plt.title("Temperature Trend")

plt.subplot(1,2,2)
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temp")

plt.tight_layout()
plt.savefig("combined_plots.png")
plt.show()

# -------------------------------
# Task 5: Export Clean Data
# -------------------------------

df.to_csv("cleaned_weather_data.csv", index=False)
print("\nFiles Generated Successfully!")
