# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 17:21:14 2015

@author: dak
"""

import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT 
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly 
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''
    riders = 0
    old_key = None

    for line in sys.stdin:
        
        data = line.strip().split("\t")
        
        # throw out invalid data
        if len(data) != 2:
            continue
        
        # this_key ends up being data[0]
        # count ends up being data[1], total numer of hourly riders
        this_key, count = data
        
        # aadhaar_generated will be the sum of all the counts for
        # all the records for a particular district
     
        # data comes to us sorted, did we switch to the next key
        # if I switched keys, print out the key and its summated counter
        if old_key and old_key != this_key:
            # we've switched to a new key
            print "{0}\t{1}".format(old_key, riders)
            # reset our summation counter
            riders = 0

        old_key = this_key
        riders += float(count)
    
    # because there is no next key after the last key 
    # without this we would not include the last row
    if old_key != None:
        print "{0}\t{1}".format(old_key, riders)

        
reducer()
