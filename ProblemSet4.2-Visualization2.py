# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pandas import *
from ggplot import *
import matplotlib.pyplot as plt

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
    # geom_histogram is an alias for geom_bar plus stat_bin

    # average exits hourly
    # pull out only those two fields
    # this prints 131951 rows of data, two columns, hour and exits
    turnstile_weather = turnstile_weather[['Hour','EXITSn_hourly']]
    #print turnstile_weather
         
    # counts on the Y axis
    # this prints 23 entries
    # one per hour and the average of exits for that hour
    grouped = turnstile_weather.groupby('Hour', as_index=False).mean()
    print grouped.describe()
    print grouped
    
    
    # which hour has the max average exits
    myresult = grouped['EXITSn_hourly'].argmax()
    print "max result is ",myresult
    print "MAX row is",grouped.ix[myresult,:]
    
    # which hpur has the min average exits
    myresult = grouped['EXITSn_hourly'].argmin()
    print "min  is ",myresult
    print "MIN row is",grouped.ix[myresult,:]    
    
    # stat='bar' is a count of cases in each group
    # stat='identity' is the values in a column of the data frame
    
    # bar graph
    plot = ggplot(grouped, aes('Hour','EXITSn_hourly'))  + \
           geom_bar(stat='bar', colour="blue", fill='lightblue') + \
           ggtitle('Average Exits by Hour')  + \
           xlab('Hour') + ylab('Average Exits')
    print plot

     
    # point plot
    gg = ggplot(grouped, aes('Hour','EXITSn_hourly')) +  \
            geom_point(color='RED') + geom_line(color='RED') + \
            ggtitle( 'Average by hour') + \
            xlab('Hour') + ylab('Average exits')
    print gg

    
filename="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"
turnstile = pandas.read_csv(filename) 
result = plot_weather_data(turnstile)
#print result

