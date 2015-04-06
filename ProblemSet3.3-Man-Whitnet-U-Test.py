# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:25:22 2015

@author: dak
"""

import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means2(turnstile_weather):
    
    turnstile_weather_no_rain  = turnstile_weather[turnstile_weather.rain == 0]
    turnstile_weather_rain = turnstile_weather[turnstile_weather.rain == 1]

    entries_no_rain = np.array(turnstile_weather_no_rain['ENTRIESn_hourly'])
    entries_with_rain = np.array(turnstile_weather_rain['ENTRIESn_hourly'])

    without_rain_mean = np.mean(entries_no_rain[~np.isnan(entries_no_rain)])
    with_rain_mean = np.mean(entries_with_rain[~np.isnan(entries_with_rain)])

    U,p = scipy.stats.mannwhitneyu(entries_no_rain, entries_with_rain)

    return with_rain_mean, without_rain_mean, U, p

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
 
    with_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 1]
    without_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain == 0]
    print "records with rain", len(with_rain)
    print "records without rain", len(without_rain)
    
    # is the data normal, scipy shapiro test
    print "shapiro result", (scipy.stats.shapiro(turnstile_weather["ENTRIESn_hourly"]))
    print "shapiro with rain result", (scipy.stats.shapiro(with_rain))
    print "shapiro without rain result", (scipy.stats.shapiro(without_rain))
    
    # is the data normal, scipy normaltest
    (k, pvalue) = scipy.stats.normaltest(turnstile_weather["ENTRIESn_hourly"])
    print "pvalue for ENTRIESn_hourly", pvalue
    (k, pvalue) = scipy.stats.normaltest(with_rain)
    print "pvalue for with_rain", pvalue
    (k, pvalue) = scipy.stats.normaltest(without_rain)
    print "pvalue for without _rain", pvalue
    print "if pvalue M 0.05, then it is not normal distribution"
    
    # run the Mann Whitney U test
    with_rain_mean = np.mean(with_rain)
    without_rain_mean = np.mean(without_rain)
    U, p = scipy.stats.mannwhitneyu(with_rain, without_rain)  
    
    
    # this result is from teh class grader
    #(1105.4463767458733, 1090.278780151855, 1924409167.0, 0.024999912793489721)
    
    # this result is from running in Spyder
    #(1105.4463767458733, 1090.278780151855, 1924409167.0, 0.019309634413792565)

    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader
    
file_path="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"    
turnstile = pandas.read_csv(file_path) 
print"RUN ONE"
print mann_whitney_plus_means(turnstile) 

print "RUN TWO"
print mann_whitney_plus_means2(turnstile) 

