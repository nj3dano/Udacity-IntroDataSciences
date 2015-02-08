# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 16:46:58 2015

@author: dak
"""

import json
import requests
import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    # note: this is a quiz answer, the URL is passed in for you
    # for this exercise you do not need an API key
    # you cannot run it in spider as is
    
    data = requests.get(url).text
    data = json.loads(data)
    
    ###################################################
    # How I worked it out
        
    #pp = pprint.PrettyPrinter(indent=2)
    #pp.pprint(data)
    
    # you have elements ordered by ranking
    # you have @attr, artist, listeners  etc
    #artists = data['topartists']
    #print artists
    
    # pull out just the artist information
    #justArtists = artists['artist']
    #print justArtists
    
    # now pull out the first in the list
    #theTop = justArtists[0]
    #print theTop
    
    # now pull out the name
    #theName = theTop['name']
    #print theName
    
    ###################################################
    
    # the answer is Arctic Monkeys
    theName=data['topartists']['artist'][0]['name']
    
    return theName # return the top artist in Spain
