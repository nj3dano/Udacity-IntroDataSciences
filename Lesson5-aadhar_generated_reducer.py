# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 13:12:23 2015

@author: dak
"""
import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    
    aadhaar_generated = 0
    old_key = None
        
    # the input here comes from the mapper, tab separated, 2 values
    for line in sys.stdin:
        
        #logging.info("line is ")
        #logging.info(line)
        
        # tokenize the line of data, this is a tab as put in by the mapper
        # now data is the district and the aadhar_generated
        data = line.strip().split("\t")
       
        # throw out invalid data
        if len(data) != 2:
            continue
        
        # this_key ends up being data[0]
        # count ends up being data[1], total numer of addhar_generated in data
        this_key, count = data
        
        # aadhaar_generated will be the sum of all the counts for
        # all the records for a particular district
     
        # data comes to us sorted, did we switch to the next key
        # if I switched keys, print out the key and its summated counter
        if old_key and old_key != this_key:
            # we've switched to a new key
            print "{0}\t{1}".format(old_key, aadhaar_generated)
            # reset our summation counter
            aadhaar_generated = 0

        old_key = this_key
        aadhaar_generated += float(count)
    
    # because there is no next key after the last key 
    # without this we would not include the last row
    if old_key != None:
        print "{0}\t{1}".format(old_key, aadhaar_generated)
        
reducer()