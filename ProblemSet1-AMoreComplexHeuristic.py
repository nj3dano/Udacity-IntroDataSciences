# -*- coding: utf-8 -*-
"""
Spyder Editor
dak 2/4/17 Problem Set 1 - A more complex Heuristic
"""
import numpy
import pandas
#import statsmodels.api as sm

def complex_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associated
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a more sophisticated algorithm
    that will use the passengers' gender and their socioeconomical class and age 
    to predict if they survived the Titanic diaster. 
    
    You prediction should be 79% accurate or higher.
    
    Here's the algorithm, predict the passenger survived if:
    1) If the passenger is female or
    2) if his/her socioeconomic status is high AND if the passenger is under 18
    
    Otherwise, your algorithm should predict that the passenger perished in the disaster.
    
    Or more specifically in terms of coding:
    female or (high status and under 18)
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".
    
    You can access the socioeconomic status of a passenger via passenger['Pclass']:
    High socioeconomic status -- passenger['Pclass'] is 1
    Medium socioeconomic status -- passenger['Pclass'] is 2
    Low socioeconomic status -- passenger['Pclass'] is 3

    You can access the age of a passenger via passenger['Age'].
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survived or 0 otherwise. 

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        
        # 
        # your code here
        # for example, assuming that passengers who are male
        # and older than 18 surived:
        #     if passenger['Sex'] == 'male' or passenger['Age'] < 18:
        #         predictions[passenger_id] = 1
        # 
        if passenger.Sex == 'female':
            predictions[passenger_id] = 1  # lived
        elif passenger.Age < 18 and passenger.Pclass == 1:
            predictions[passenger_id] = 1  # lived
        else:
            predictions[passenger_id] = 0  # died
            
    return predictions
    
# I download the data set locally from:
# http://www.kaggle.com/c/titanic-gettingStarted/data?train.csv
# At first, I set the file_path as the full path name 
# file_path='C:/Users/dak/Udacity-IntroDataSciences/train.csv'
# but the read above is reading using relative path and even though
# my working directory seemed right, it gave an IOError on read until
# I just passed in the file name rather than the full path.  The file
# does exist in my working directory
file_path="train.csv"
result = complex_heuristic(file_path)
print result