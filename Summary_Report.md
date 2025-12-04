# Weather Data Analysis – Summary Report

1. Introduction
This mini project is a part of my Python course (Programming for Problem Solving).
The aim of this project was to analyse a small real-world weather dataset and understand basic data handling, statistics, and visualization using Python.
For this project, I used a 30-day weather dataset that contains daily temperature, humidity, and rainfall values.

2. Dataset Description
The dataset contains 30 days of weather records.
Columns used:
date – the day of the record
temperature – daily temperature
humidity – daily humidity
rainfall – daily rainfall
The dataset was saved as CleanWeatherData.csv, and missing values were filled appropriately.

3. Steps Performed
✔ 1. Loading the Data
I loaded the CSV file using Pandas and checked the first few rows, info, and statistics.
✔ 2. Cleaning the Data
Converted the date column to proper datetime format
Kept only the required columns
Handled missing data:
Filled temperature and humidity with their mean
Filled rainfall values with 0
✔ 3. Statistical Analysis
I calculated important statistics such as:
Mean temperature
Minimum and maximum temperature
Standard deviation
Monthly averages (since dataset is only 30 days, 1 month)
✔ 4. Visualizations
I created simple plots using Matplotlib:
Line chart → daily temperature trend
Bar chart → rainfall
Scatter plot → humidity vs temperature
Combined plot → (temperature trend + scatter plot)
These graphs help in understanding trends more clearly.

4. Observations / Insights
Temperature varied moderately over the 30 days.
Humidity showed a direct relationship with temperature in some days.
Rainfall was low and on a few days only.
The dataset helped me understand how weather patterns behave even in a short duration.

5. Conclusion
This project helped me practice:
1. Reading and cleaning data using Pandas
2. Applying simple statistics using NumPy
3. Building basic visualizations in Matplotlib
4. Exporting clean data and understanding weather patterns

It also gave me confidence in handling real-world datasets using Python.
This mini project helped understand data cleaning, analysis, visualization, and exporting results using Pandas, NumPy, and Matplotlib.
