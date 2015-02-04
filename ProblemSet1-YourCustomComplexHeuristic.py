# -*- coding: utf-8 -*-
"""
Spyder Editor
dak 2/4/17 Problem Set 1 - Your custom Heuristic
"""
import numpy
import pandas
#import statsmodels.api as sm

def custom_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associated
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a custom heuristic that will take
    in some combination of the passenger's attributes and predict if the passenger
    survived the Titanic diaster.

    Can your custom heuristic beat 80% accuracy?
    
    The available attributes are:
    Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)
                    
    SPECIAL NOTES:
    Pclass is a proxy for socioeconomic status (SES)
    1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

    Age is in years; fractional if age less than one
    If the age is estimated, it is in the form xx.5

    With respect to the family relation variables (i.e. SibSp and Parch)
    some relations were ignored. The following are the definitions used
    for SibSp and Parch.

    Sibling:  brother, sister, stepbrother, or stepsister of passenger aboard Titanic
    Spouse:   husband or wife of passenger aboard Titanic (mistresses and fiancees ignored)
    Parent:   mother or father of passenger aboard Titanic
    Child:    son, daughter, stepson, or stepdaughter of passenger aboard Titanic
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survvied or 0 otherwise. 

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
        # Lived
        # female and embarked Q/C, or, female and pclass 1 or 2
        # male under 30 and pclass 1
        passenger_id = passenger['PassengerId']
        if passenger.Sex == 'female':
            if passenger.Embarked == 'Q' or passenger.Embarked == 'C':
                predictions[passenger_id] = 1  # female lived
            elif passenger.Pclass < 3:
                predictions[passenger_id] = 1  # female lived
            else:
                predictions[passenger_id] = 0  # female died
        elif passenger.Age < 30 and passenger.Pclass == 1:
            predictions[passenger_id] = 1  # male lived
        else:
            predictions[passenger_id] = 0  # male died
            
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
result = custom_heuristic(file_path)
print result