# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 22:07:27 2015

@author: dak
"""

from pandas import *
from ggplot import *

import pandas

def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot2.
    #
    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://www.dropbox.com/s/wn43cngo2wdle2b/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions. For example, 
    # ggplot(data, aes(xvar, yvar, color=category_var)). This should help you 
    # in this exercise.

    df = pandas.read_csv(hr_by_team_year_sf_la_csv)
    
    #sfn = df[df.teamID == 'SFN']
    #lan = df[df.teamID == 'LAN']
      
    gg = ggplot(df, aes('yearID', 'HR', color='teamID')) +  \
            geom_point() + geom_line() + \
            ggtitle( 'Total HRs by year') + xlab('Year') + ylab('HR')
    
    return gg

filename="C:/Users/dak/Documents/Udacity.IntroDataSciences/hr_by_team_year_sf_la.csv"
result = lineplot_compare(filename)
print result