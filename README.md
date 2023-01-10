# BootcampModule9
SurfsUp

## Overview of the analysis.

-  The goal of this project is to develop a business plan for a surfing and ice cream combination store in Oahu, Hawaii.

-  Utilizing temperature and weather data from monitoring stations accross the island over the last 7 years, we were able to extract and extrapolate the viability of the plan.

   

### Results:

1- *Precipitation*

- To get a snapshot of the weather data, we sample the oldest year of weather data to begin our filtering process.

```
# Design a query to retrieve the last 12 months of precipitation data and plot the results. 
#Starting from the last data point in the database. 
##prev_year=dt.date(2017, 8, 23)

# Calculate the date one year from the last date in data set.
prev_year = dt.date(2017, 8, 23) -dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
results = []
results = session.query(Measurement.date, Measurement.prcp)
#add a filter for the previous year
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year)
#extract all results from query and add the to list
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

# Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(results, columns=['date','precipitation'])
# Sort the dataframe by date
df.set_index(df['date'], inplace=True)
# Use Pandas Plotting with Matplotlib to plot the data
df.plot()
```
- ![image](https://github.com/LordNebbs/BootcampModule9/blob/8ed0b8abaa01a566c76eeaf67600a7c66d0b35df/data/1yearprecip.png)

This helps visualize that it rains fairly consistently with an average of 3" throughout the year with rates as high as 6+" around July and November. While this is helpful we have to remember this is a snapshot of just one year in a dataset of nine and need to consider that there may be outlier data in this set.


2- *Temperature*
```
# 1. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
june_temp = session.query(Measurement.tobs, Measurement.date).filter(extract('month', Measurement.date)==6).all()

print(june_temp)

june_df = pd.DataFrame(results_june, columns=['June Temp', 'Date'])
june_df.describe()

```
We then use SQLite to right a query to find the temperature ranges for June (show above) and repeating the process for Dec.

- ![image](https://github.com/LordNebbs/BootcampModule9/blob/d5852dc4d59381ab1587479e512304e95e665cde/data/June%20Temps.png)
![image](https://github.com/LordNebbs/BootcampModule9/blob/d5852dc4d59381ab1587479e512304e95e665cde/data/June%20Temps.png)

From there we can see that even in the hottest and coldest months of the year the range of temperture never quite deviates far from 73 degrees. 


3- Look for averages over the entire dataset

```
import datetime as dt
import matplotlib.pyplot as plt

# Calculate the date 5 years ago and pull datapoints for 5 years
prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=(365*5))

# Perform a query to retrieve the data and precipitation scores
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

# Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(results, columns=['date','precipitation'])

#format errors
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Extract the month from the date column and create a new column called month
df['month'] = df['date'].dt.month

# Group the data by month and compute the mean precipitation for each month
monthly_mean = df.groupby('month')['precipitation'].mean()

# Create an empty list to store the plot objects
plots = []

# Iterate over the months
for month in monthly_mean.index:
    # Filter the data for the current month
    df_month = df.loc[df['month'] == month]
    
    # Compute the mean precipitation for the current month
    mean_precipitation = df_month['precipitation'].mean()
    
    # Create a bar plot for the current month
    plot = plt.bar(month, mean_precipitation)
    
    # Add the plot object to the list
    plots.append(plot)

    # Add a label to the x-axis
    plt.xlabel('Month')

    # Add a label to the y-axis
    plt.ylabel('Precipitation (inches)')

# Show the plot
plt.show()
```

- ![image](https://github.com/LordNebbs/BootcampModule9/blob/fbd7635f23305c2a1eb60f63e68781c1c970e1d0/data/precip9year.png)

Here we see that on any given day, we are averaging 1/4" of rain no atter what time of year it is and only really have to worry about rain being heavier in July-Novemeber. This supports the initial sample we took.
# Summary:

-   Based on the results, the client should have no issues opening a beach shop if their only considersations is rain and the cold. 

# Suggestions
- Another consideration might be including census data for the beaches to see where opening on Oahu would be most cost effective. 
