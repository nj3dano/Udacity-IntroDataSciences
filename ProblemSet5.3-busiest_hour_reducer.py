# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 18:16:47 2015

@author: dak
"""
import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the 
    date and time with the most entries) for each turnstile unit. Ties should 
    be broken in favor of datetimes that are later on in the month of May. You 
    may assume that the contents of the reducer will be sorted so that all entries 
    corresponding to a given UNIT will be grouped together.
    
    The reducer should print its output with the UNIT name, the datetime (which 
    is the DATEn followed by the TIMEn column, separated by a single space), and 
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    max_entries = 0
    old_key = None
    datetime = ''

    for line in sys.stdin:
        data = line.strip().split("\t")
        
        # throw out invalid data, 4 columns this time
        if len(data) != 4:
            continue
        
        # this_key ends up being data[0]
        # count ends up being data[1], total numer of hourly riders
        this_key, count, myDate, myTime = data
           
        # data comes to us sorted, did we switch to the next key
        # if I switched keys, print out the key and its average
        if old_key and old_key != this_key:
            # we've switched to a new key
            print "{0}\t{1}\t{2}".format(old_key, datetime, max_entries)
            # reset our counters
            max_entries = 0
            datetime=''
            
        old_key = this_key
        
        # is this current hourly count greater than the stored max so far ?
        if float(count) > float(max_entries):
            max_entries = count
            datetime = "{0} {1}".format(myDate, myTime)
        
        # tie breaker
        if float(count) == float(max_entries):
            # this record's datetime is later, this record wins the tie
            thisOne = "{0} {1}".format(myDate, myTime)
            if thisOne > datetime:
                datetime = thisOne
                
        # id current hourly count is less than the stored max, keep the
        # stored max, nothing further needed for this record
    
    # because there is no next key after the last key 
    # without this we would not include the last row
    if old_key != None:
       print "{0}\t{1}\t{2}".format(this_key, datetime, max_entries)

reducer()
