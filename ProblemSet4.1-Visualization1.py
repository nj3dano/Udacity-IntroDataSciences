# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pandas import *
from ggplot import *
import pandasql

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
    
    # plot hourly entries based on Subway Station
    # pull out only those two fields
    turnstile_weather = turnstile_weather[['UNIT','ENTRIESn_hourly']]
       
    # add up the entries for each station
    grouped = turnstile_weather.groupby('UNIT', as_index=False).sum()
    #print grouped
    print grouped.describe()
    
    # which station has the max entries
    myresult = grouped['ENTRIESn_hourly'].argmax()
    #print "max result is ",myresult
    print "MAX row 159 is",grouped.ix[myresult,:]
    
    # which station has the min entries
    myresult = grouped['ENTRIESn_hourly'].argmin()
    #print "min  is ",myresult
    print "MIN row 447 is",grouped.ix[myresult,:]
       
    # get a smaller set of the dat (or not)  
    #groupedSmaller=grouped.head(20)
    groupedSmaller=grouped
    
    # stat='bar' is a count of cases in each group
    # stat='identity' is the values in a column of the data frame
       
    ##############################################
    # HISTOGRAM
    ##############################################
    # geom_histogram is an alias for geom_bar plus stat_bin
    # this makes the bin off,  need to understand what the correct value for
    # bin width is.  Also, if you do not use stat=identity, the
    # histogram, is a very different picture too
    #geom_histogram(binwidth=20) + \
     
    plot = ggplot(groupedSmaller, aes(x='UNIT', y='ENTRIESn_hourly')) + \
            geom_histogram(stat='bar', colour="green", fill='lightgreen') + \
            ggtitle('Entries by Station')  + \
            xlab('STATION') + ylab('ENTRIES')
    print plot

    ##############################################
    # GEOM_BAR
    ##############################################      
    plot = ggplot(groupedSmaller, aes(x='UNIT', y='ENTRIESn_hourly'))  + \
            geom_bar(stat='bar', colour="blue", fill='lightblue') + \
            ggtitle('Entries by Station')  + \
            xlab('STATION') + ylab('ENTRIES')
    print plot
    
filename="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"
turnstile = pandas.read_csv(filename) 
result = plot_weather_data(turnstile)
#print result

