# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 15:00:25 2015

@author: dak
"""

import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

    #WRITE YOUR CODE HERE

    # note:  This is the solution for the quiz, you cannot actually run
    # this as is because we don't  have the file, and we didn't set
    # path_to_csv and path_to_new_csv
    baseball_data = pandas.read_csv(path_to_csv)
    baseball_data['nameFull'] = baseball_data.nameFirst +' ' + baseball_data.nameLast
    baseball_data.to_csv(path_to_new_csv)
    