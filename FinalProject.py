# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:25:22 2015

@author: dak
"""

import numpy as np
import scipy
import scipy.stats
from pandas import *
from ggplot import *
import matplotlib.pyplot as plt


def mytry(turnstile_weather):
     
    #######################################################
    # pull out weather data
    # with_rain is a list of 131951 single entries
    # without_rain is a list of 131951 single entries
    # rdf is [131951 rows x 2 columns]
    #        rain  without_rain
    #0          0             0
    #1          0           217
    #######################################################
    with_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 1]
    without_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 0] 
    #print with_rain.head(10)

    #######################################################    
    # first plot, by hour
    #######################################################
    plotA = ggplot(turnstile_weather, aes('Hour', 'ENTRIESn_hourly', fill ='rain', color='rain'))\
        + geom_histogram() \
        + scale_color_manual(values=['black', 'red']) \
        + xlab("Which hour of the day") \
        + ggtitle("Ridership by hour - Rain in black: No Rain in Red" )\
        + ylab("Entries")
    print plotA
    
    #######################################################    
    # second histogram, entries rain not rain
    # histogram view is not spread enough to see differences
    #######################################################    
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 1]).hist(bins=400)
    print plt
 
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 0]).hist(bins=400)
    print plt

    ####################################################### 
    # third plot spread out, entries rain not rain
    ####################################################### 
    rainData = {'rain':Series(with_rain),
                'without_rain': Series(without_rain)}
    rdf = DataFrame(rainData) 
    rdf['rain'] = rdf['rain'].fillna(0)
    rdf['without_rain'] = rdf['without_rain'].fillna(0)  
       
    # combine it all into one line if you want
    #    rdf = DataFrame({
    #   "rain": turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly'],
    #   "no_rain": turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']
    #}).fillna(0)
    
    #######################################################    
    #  reshape data from wide to long format
    # [263902 rows x 2 columns]
    #            variable  value
    #               rain      0
    #263901  without_rain     0
    #######################################################
    rdf = melt(rdf)
    #print type(rdf)
    
    #######################################################
    # plot the data in long format on same plot
    # Note that to differentiate between multiple categories on 
    # the same plot, we  pass color in with the other arguments
    # to aes, rather than in our geometry functions.
    # xvar and yvar are going to be columns in the data frame
    ####################################################### 
    plotD = ggplot(aes(x ='value', fill='variable', color='variable'), data = rdf) \
      + scale_color_manual(name="legend title",values=['black', 'red']) \
      + geom_histogram( alpha=0.5, binwidth=400, position="dodge") \
      + scale_y_log() \
      + ylab("Frequency of occurrence") \
      + xlab("Entries") \
      + ggtitle("Entries vs Frequency")

    print plotD
        
file_path="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"    
turnstile = pandas.read_csv(file_path) 
mytry(turnstile) 
#print mytry(turnstile) 

