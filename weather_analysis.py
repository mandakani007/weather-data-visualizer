# --------------------------------------------
# Weather Data Visualizer - Mini Project
# Name: Mandakani
# --------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Task 1: Load Dataset
# -------------------------------

df = pd.read_csv("weather_data_raw.csv")
print("\nHead of Data:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())

# -------------------------------
# Task 2: Cleaning
# -------------------------------

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

# selecting required columns
df = df[["date", "temperature", "humidity", "rainfall"]]

# fill missing values
df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
df["humidity"] = df["humidity"].fillna(df["humidity"].mean())
df["rainfall"] = df["rainfall"].fillna(0)

# -------------------------------
# Task 3: Stats
# -------------------------------

print("\nTemperature Mean:", df["temperature"].mean())
print("Temperature Max :", df["temperature"].max())
print("Temperature Min :", df["temperature"].min())
print("Std :", np.std(df["temperature"]))

df["month"] = df["date"].dt.month
monthly_stats = df.groupby("month")[["temperature", "rainfall", "humidity"]].mean()
print("\nMonthly Stats:")
print(monthly_stats)

# -------------------------------
# Task 4: Visuals
# -------------------------------

# Line plot
plt.plot(df["date"], df["temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("images/daily_temperature.png")
plt.close()

# Monthly rainfall bar
plt.bar(monthly_stats.index, monthly_stats["rainfall"])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.savefig("images/monthly_rainfall.png")
plt.close()

# Scatter
plt.scatter(df["temperature"], df["humidity"])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("images/humidity_vs_temp.png")
plt.close()

# Combined
plt.subplot(1,2,1)
plt.plot(df["date"], df["temperature"])
plt.title("Temperature Trend")

plt.subplot(1,2,2)
plt.scatter(df["temperature"], df["humidity"])
plt.title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("images/combined_plots.png")
plt.close()

# -------------------------------
# Task 5: Grouping
# -------------------------------

df["season"] = df["month"].map({
    12:"Winter",1:"Winter",2:"Winter",
    3:"Spring",4:"Spring",5:"Spring",
    6:"Summer",7:"Summer",8:"Summer",
    9:"Autumn",10:"Autumn",11:"Autumn"
})

season_stats = df.groupby("season")[["temperature","rainfall","humidity"]].mean()
print("\nSeasonal Stats:")
print(season_stats)

# -------------------------------
# Task 6: Export Cleaned Data
# -------------------------------

df.to_csv("cleaned_weather_data.csv", index=False)
monthly_stats.to_csv("monthly_summary.csv")

print("\nDone! Plots saved and cleaned data exported.")
