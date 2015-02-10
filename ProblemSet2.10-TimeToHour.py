# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 18:54:56 2015
# runfile'C:/Users/dak/Udacity-IntroDataScience/ProblemSet2-NumberOfRainyDays.py'
# wdir='C:/Users/dak/Udacity-IntroDataScience'

@author: dak
"""
import pandas

def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    "00:00:00" (hour:minutes:seconds)
    
    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21
        
    Please return hour as an integer.
    '''
    # solutions
    # hour = int(time.split(':')[0])
    # hour = pandas.to_datetime(time).hour
    
    # parse string
    dt_str=time.split(':')
    hour = int(dt_str[0])
    return hour
    
# this is the quiz result for class
# you cannot run it in spider unless you add the logic
# to pull and construct the filenames etc.
