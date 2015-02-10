# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 18:54:56 2015
# runfile'C:/Users/dak/Udacity-IntroDataScience/ProblemSet2-NumberOfRainyDays.py'
# wdir='C:/Users/dak/Udacity-IntroDataScience'

@author: dak
"""
import datetime

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There is a useful function in the datetime library called strptime. 
    More info can be seen here:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    date_formatted = # your code here
    return date_formatted    # class datetime.datetime
    # A combination of a date and a time. Attributes: year, month, day,
    # hour, minute, second, microsecond, and tzinfo.
    
    # The method strptime() parses a string representing a time according to a format

    #dateInput = datetime.datetime.strptime(date,"%m-%d-%y")
    #date_formatted = dateInput.strftime("%Y-%m-%d")
    
    date_formatted = datetime.datetime.strptime(date,"%m-%d-%y").strftime("%Y-%m-%d")

    
# this is the quiz result for class
# you cannot run it in spider unless you add the logic
# to pull and construct the filenames etc.
