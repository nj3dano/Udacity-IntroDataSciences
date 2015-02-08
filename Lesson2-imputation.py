# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 17:24:53 2015

@author: dak
"""

from pandas import *
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colunm in the baseball data frame by
    # calling baseball['weight']

    #YOUR CODE GOES HERE, imputation 
    baseball = pandas.read_csv(filename)
    averageWeight=numpy.mean(baseball['weight'])
    baseball['weight'] = baseball['weight'].fillna(averageWeight)
    
    # this is the quiz answer, does not run in spyer unless
    # you correctly setup the filename etc
    
    return baseball