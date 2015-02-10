# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 18:54:56 2015
# runfile'C:/Users/dak/Udacity-IntroDataScience/ProblemSet2-NumberOfRainyDays.py'
# wdir='C:/Users/dak/Udacity-IntroDataScience'


@author: dak
"""

import pandas
import pandasql


def avg_min_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data. More specifically you want to find the average
    minimum temperature on rainy days where the minimum temperature
    is greater than 55 degrees.
    
    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply 
    where maxtempi = 76.
    
    You can see the weather data that we are passing in below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)

    q = """
    select avg(cast (mintempi as integer)) from weather_data
    where mintempi > 55 and rain = 1;
    """
    
    #Execute your SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(q.lower(), locals())
    return avg_min_temp_rainy

    
filename="C:/Users/dak/Documents/Udacity.IntroDataSciences/weather_underground.csv"
result = avg_min_temperature(filename)
print result