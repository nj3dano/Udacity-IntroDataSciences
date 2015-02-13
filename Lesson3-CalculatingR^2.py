# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:42:21 2015

@author: dak
"""

import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    
    # numpy.sum((data-predictions)**2)
    # or sum([(data - predictions)**2 for data in predictions])

    #calculated R^2 value is: 0.318137233709
    #average = np.mean(data)
    #numerator = np.sum((data - predictions)**2)
    #demonimator = np.sum((data - average)**2)
    #r_squared = 1.0 - (numerator/demonimator)
    
    r_squared = 1.0 - ( (np.sum((data - predictions)**2)) /
                        (np.sum((data - (np.mean(data)))**2)) )
    return r_squared