# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 18:54:56 2015
# runfile'C:/Users/dak/Udacity-IntroDataScience/ProblemSet2-NumberOfRainyDays.py'
# wdir='C:/Users/dak/Udacity-IntroDataScience'


@author: dak
"""
    
import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        
        updatedFileName = "updated_" + name
        with open(updatedFileName, 'wb') as OutputFile:
            writer = csv.writer(OutputFile)   
            with open(name, 'rb') as InputFile:
                reader = csv.reader(InputFile)
                for row in reader:
                                    
                    # The first three elements in the input line
                    # (A002,R051,02-00-00) are repeated for each
                    # of the 8 lines in the output file. Then the
                    # data is in sets of 5
                    PrefixElementCount=3
                    RepeatedElementCount=5
                
                    prefix = row[0:PrefixElementCount]
                                   
                    # start at the fourth element, and take the next 5
                    # which repeat in sets of five until the end of the row
                    rowTraverse=PrefixElementCount; 
                    myCount = len(row) - PrefixElementCount # account for starting at 4th
                    while myCount > 0:
                       remainderRow=row[rowTraverse:(rowTraverse+RepeatedElementCount)]
                       writer.writerow( (prefix + remainderRow) )
                        
                       rowTraverse += RepeatedElementCount
                       myCount -= RepeatedElementCount
                        
# this is the quiz result for class
# you cannot run it in spider unless you add the logic
# to pull and construct the filenames etc.
