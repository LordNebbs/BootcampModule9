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
- ![image](https://github.com/LordNebbs/BootcampModule7/blob/97a6a739d470cff38a49649ffe2158cd9dbf701d/Tables/retiring%20titles.png)

This helps visualize that it rains fairly consistently with an average of 3" throughout the year with rates as high as 6+" around July and November. While this is helpful we have to remember this is a snapshot of just one year in a dataset of nine and need to consider that there may be outlier data in this set.


2- *Temperature*
```
# 1. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
june_temp = session.query(Measurement.tobs, Measurement.date).filter(extract('month', Measurement.date)==6).all()

print(june_temp)

june_df = pd.DataFrame(results_june, columns=['June Temp', 'Date'])
june_df.describe()

```
We then use SQLite to right a query to 

3- *Retiring titles*

- ![image](https://github.com/LordNebbs/BootcampModule7/blob/97a6a739d470cff38a49649ffe2158cd9dbf701d/Tables/retiring%20titles.png)

This clearly shows that PH is going to need to hire agressively to fill the massive void of talent that is immenently coming. 

4- *Mentorship eligibility*

-  Mentorship is a great way to help get the next generation up to speed and make sure that the talent and knowledge cultivated within the company is not lost. However when using a 10 year bufffer from the current retirement cutoff dates, on average accross the 72458, 3.2% per title are eligible to mentor younger employees. Assistant Engineers are the most covered with 7.15% coverage based on those leaving where Senior Engineers have 0.65% coverage.

![image](https://github.com/LordNebbs/BootcampModule7/blob/main/Tables/Silver%20Exit.png)

-   The ammount of "Brain Drain" is staggering and a better mentoring program is needed and perhaps the criteria and the mapping of the mentoring program to the titles replaced, needs to be reviewed to match the demands at Pewlett Packard.


# Summary:

-   Based on the results, PH is facing a crisis. If something is not done to address the massive workforce loss, whoever is left to fill in their shoes will not only be potentially understaffed, but unequipped to handle problems faced as the people who pioneered the departments are no longer available.

# Suggestions
1- Retooling the milestone triggers for mentorship needs to be explored. Query and table to show the people ahead of retirement time so that the retirement date would match new people mentored or ready for work as per HR policies and goals. This way the retirement exit will not be as big.

2- More titles that will retire can be eligible for mentorship. Direct quota increase or criterias that allow more retiring titles to be eligible for mentorship. 

