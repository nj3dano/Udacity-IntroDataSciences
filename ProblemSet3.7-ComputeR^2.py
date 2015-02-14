# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 11:59:44 2015

@author: dak
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys

def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    # Your calculated R^2 value is: 0.318137233709
    r_squared = 1.0 - ( (np.sum((data - predictions)**2)) /
                        (np.sum((data - (np.mean(data)))**2)) )
    
    return r_squared