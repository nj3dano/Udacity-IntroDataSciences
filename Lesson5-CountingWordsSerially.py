# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 11:56:02 2015

@author: dak
"""

import logging
import sys
import string
import re

#from util import logfile

#logging.basicConfig(filename=logfile, format='%(message)s',
#                   level=logging.INFO, filemode='w')


def word_count():
    # For this exercise, write a program that serially counts the number of occurrences
    # of each word in the book Alice in Wonderland.
    #
    # The text of Alice in Wonderland will be fed into your program line-by-line.
    # Your program needs to take each line and do the following:
    # 1) Tokenize the line into string tokens by whitespace
    #    Example: "Hello, World!" should be converted into "Hello," and "World!"
    #    (This part has been done for you.)
    #
    # 2) Remove all punctuation
    #    Example: "Hello," and "World!" should be converted into "Hello" and "World"
    #
    # 3) Make all letters lowercase
    #    Example: "Hello" and "World" should be converted to "hello" and "world"
    #
    # Store the the number of times that a word appears in Alice in Wonderland
    # in the word_counts dictionary, and then *print* (don't return) that dictionary
    #
    # In this exercise, print statements will be considered your final output. Because
    # of this, printing a debug statement will cause the grader to break. Instead, 
    # you can use the logging module which we've configured for you.
    #
    # For example:
    # logging.info("My debugging message")
    #
    # The logging module can be used to give you more control over your
    # debugging or other messages than you can get by printing them. Messages 
    # logged via the logger we configured will be saved to a
    # file. If you click "Test Run", then you will see the contents of that file
    # once your program has finished running.
    # 
    # The logging module also has other capabilities; see 
    # https://docs.python.org/2/library/logging.html
    # for more information.

    word_counts = {}

    # in class, this was fed via stdin
    # change this to read from the file in spyder
    #for line in sys.stdin:
        #data = line.strip().split(" ")

    filename="C:/Users/dak/Documents/Udacity.IntroDataSciences/intro_to_ds_programming_files/lesson_5/word_count_no_mr_quiz/aliceInWonderland.txt"
    f = open(filename)
    
    for line in f:

        # tokenize the line of data
        data = line.strip().split(" ")
   
       # cycle through the words        
        for word in data:
            # for regex: \W matches not alpha and not underscores
            # you need \W_ to remove all non aplhanumerics
            # add the plus to match one or more occurrences
            # then convert to lower case
            clean_word = re.sub(r'[\W_]+', '', word.lower())
            #print "clean word is",clean_word
            
            # another way to clean the data
            #clean_word = word.translate(string.maketrans("",""),string.punctuation).lower()
        
            #if clean_word in word_counts.keys():          
            if clean_word in word_counts:
                word_counts[clean_word] += 1
            else:
               word_counts[clean_word] = 1  

    f.close()    
    print word_counts

word_count()
