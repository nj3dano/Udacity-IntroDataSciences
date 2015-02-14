# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 11:30:10 2015

@author: dak
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    ##########################################################################
    # http://stackoverflow.com/questions/9141732/how-does-numpy-histogram-work
    # A bin is range that represents the width of a single bar of the
    # histogram along the X-axis. You could also call this the interval
    ##########################################################################
    # The Numpy histogram function doesn't draw the histogram, but it computes
    # the occurrences of input data that fall within each bin, which in turns
    # determines the area (not necessarily the height if the bins aren't of
    # equal width) of each bar.  EQUAL WIDTH left to right
    ##########################################################################
    #  If bins=5, for example, it will use 5 bins of equal width spread between
    # the minimum input value and the maximum input value
    ##########################################################################  
    
    
    # turnstile_weather[...] is the observed, original observed hourly data
    # turnstile_weather['ENTRIESn_hourly']
    
    # tried bins, 5, 10, 50, 80.  As you increase bins, the plot
    # takes on more of a normal curve look
        
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=50)
    return plt