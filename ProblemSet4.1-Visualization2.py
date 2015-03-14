# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 15:07:45 2015

"""

from pandas import *
from ggplot import *

def getday(date):
       return datetime.strftime(datetime.strptime(date,'%Y-%m-%d'),'%a')

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    days = []
    for mydate in turnstile_weather['DATEn']:
        days.append(getday(mydate))

    turnstile_weather.is_copy = False
    turnstile_weather.loc['DATEn'] = Series(days, 
                                     index=turnstile_weather.index)

    mygrouped = turnstile_weather.groupby('DATEn',
                                     as_index=False).sum()

    plot = ggplot(mygrouped, aes('DATEn','ENTRIESn_hourly')) + \
    geom_bar(stat= "bar") + \
    ggtitle("Entries per day") + \
    xlab("Day of month") + \
    ylab("Total entries")

    return plot

    
filename="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"
turnstile = pandas.read_csv(filename) 
result = plot_weather_data(turnstile)
print result
