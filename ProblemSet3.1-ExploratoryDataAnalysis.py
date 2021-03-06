# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:54:50 2015

@author: dak
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram2(df):
   

    bins = 150
    alpha = 0.5
    xmin = ymin = 0
    xmax = 6000
    ymax = 45000

    plt.figure()

    df['ENTRIESn_hourly'][df['rain'] == 0].hist(bins=bins, alpha=alpha)
    df['ENTRIESn_hourly'][df['rain'] == 1].hist(bins=bins, alpha=alpha)

    plt.axis([xmin, xmax, ymin, ymax])
    plt.suptitle('Histogram of ENTRIESn_hourly')
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.legend(['No rain', 'Rain'])

    return plt
    

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    #############################################################
    # THIS WORKS TOO
    # The plot method on Series and DataFrame is just a simple
    # wrapper around plt.plot()
    # isRaining is a SERIES
    # logically think of it as select[this][where this]
    #############################################################
    #plt.figure()
    #isRaining=turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 1]
    #isNotRaining=turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 0]
    #isRaining.plot(kind='hist', alpha=0.5)
    #isNotRaining.plot(kind='hist', alpha=0.5)
    #print type(isRaining)
    #print type(turnstile_weather)
    
    # DataFrame.hist, hist is a function for a dataframe not a series
    # DataFrame.hist() plots histograms of the columns on multiple subplots
    #plt.figure()
    #turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 1].hist()
    #turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 0].hist()
    #plt.legend() 
    
    # use this logic to get the  labels printed
    ax = turnstile_weather[turnstile_weather.rain == 0]['ENTRIESn_hourly'].plot(kind='hist', 
                                                                          bins = 150, 
                                                                          label='No Rain', 
                                                                          alpha = 0.5)

    ax = turnstile_weather[turnstile_weather.rain == 1]['ENTRIESn_hourly'].plot(kind='hist', 
                                                                          bins = 150, 
                                                                          label='Rain',
                                                                          alpha = 0.5)
    ax.legend()
    plt.axis([0,6000, 0, 50000])
    ax.set_ylabel('Frequency')
    ax.set_xlabel('ENTRIESn_hourly')
    ax.set_title('ENTRIESn_hourly by rain and no rain')    
        
    return plt

file_path="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"    
turnstile = pandas.read_csv(file_path) 
print entries_histogram(turnstile) 
print entries_histogram2(turnstile) 









