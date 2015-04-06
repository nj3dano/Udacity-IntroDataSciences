# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 18:10:49 2015

@author: dak
"""
import numpy as np
import pandas
from ggplot import *
import matplotlib.pyplot as plt

"""
In this question, you need to:
1) implement the compute_cost() and gradient_descent() procedures
2) Select features (in the predictions procedure) and make predictions.

"""

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    
    # numpy.sum((data-predictions)**2)
    # or sum([(data - predictions)**2 for data in predictions])

    #calculated R^2 value is: 0.318137233709
    #average = np.mean(data)
    #numerator = np.sum((data - predictions)**2)
    #demonimator = np.sum((data - average)**2)
    #r_squared = 1.0 - (numerator/demonimator)
    
    r_squared = 1.0 - ( (np.sum((data - predictions)**2)) /
                        (np.sum((data - (np.mean(data)))**2)) )
    return r_squared


def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    ##########################################################################
    # http://stackoverflow.com/questions/9141732/how-does-numpy-histogram-work
    # A bin is range that represents the width of a single bar of the
    # histogram along the X-axis. You could also call this the interval
    ##########################################################################
    # The Numpy histogram function doesn't draw the histogram, but it computes
    # the occurrences of input data that fall within each bin, which in turns
    # determines the area (not necessarily the height if the bins aren't of
    # equal width) of each bar.  EQUAL WIDTH left to right
    ##########################################################################
    # If bins=5, for example, it will use 5 bins of equal width spread between
    # the minimum input value and the maximum input value
    ##########################################################################  
        
    # turnstile_weather[...] is the observed, original observed hourly data
    # turnstile_weather['ENTRIESn_hourly']
    
    # tried bins, 5, 10, 50, 80.  As you increase bins, the plot
    # takes on more of a normal curve look
        
    plt.figure()
    residuals = (turnstile_weather['ENTRIESn_hourly'] - predictions)
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=100, color='green', alpha=0.5)
    plt.axis([-20000, 20000, 0, 60000])
    plt.xlabel('Prediction hourly Entries')
    plt.ylabel('Frequency')
    plt.title('Residuals for Linear Regression using Gradient Descent')
    
    residualsMean = np.mean(residuals)
    residualsSTD = np.std(residuals)
    print "residualsMean is ", residualsMean
    print "residualsSTD is ", residualsSTD

    return plt
    
##########################################################################
# linear regrssion functions
##########################################################################    
def normalize_features(df):
    """
    Normalize the features in the data set.
    """
    mu = df.mean()
    sigma = df.std()
    
    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                         "not be normalized. Please do not include features with only a single value " + \
                         "in your model.")
    df_normalized = (df - df.mean()) / df.std()

    return df_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    
    This can be the same code as the compute_cost function in the lesson #3 exercises,
    but feel free to implement your own.
    """
    
    # your code here
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)
    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """
    cost_history = []
    m = len(values) * 1.0
    alpha - alpha * 1.0
    
    print "dottie length of theta is ", len(theta)  
    
    for i in range(num_iterations):
        cost_history.append( (compute_cost(features, values, theta)) )
        
        Y = values
        hXi = np.dot(features, theta)
        mySummation = np.dot( (Y - hXi), features )
        theta = theta + ((alpha/m) * (mySummation))
        
    return theta, pandas.Series(cost_history)

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.20 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~15%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this computer on your own computer, locally. 
    
    
    If you'd like to view a plot of your cost history, uncomment the call to 
    plot_cost_history below. The slowdown from plotting is significant, so if you 
    are timing out, the first thing to do is to comment out the plot command again.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a 
    smaller number for num_iterations if that's the case.
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
    If you are using your own algorithm/models, see if you can optimize your code so 
    that it runs faster.
    '''
    # Select Features (try different features!)
    # this was the set I used for my first submission of the project
    #features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
    
    #these I tried
    #features = dataframe[['thunder', 'fog', 'TIMEn', 'maxtempi']]
    #features=dataframe[['rain','fog','thunder','meandewpti','meanwindspdi','precipi','Hour','meantempi','meanpressurei']]
    #features = dataframe[['Hour', 'rain', 'meanwindspdi','maxpressurei','maxtempi']]
    
    # these I used for my second submission of the project
    features = dataframe[['meantempi', 'Hour', 'rain', 'mintempi', 'maxtempi','meanwindspdi','maxpressurei', 'EXITSn_hourly']]
   
    # a reduced set of features, since my choices were highly
    # coorelated, and temp may have no impact on ridership in rain
    # reviewer also said not to use EXITSn_hourly
    #features = dataframe[['Hour', 'meanwindspdi','maxpressurei', 'rain','EXITSn_hourly']]
    #features = dataframe[['Hour', 'meanwindspdi','maxpressurei', 'rain']]
        
    # Add UNIT to features using dummy variables
    # there are 465 units, no data for R026
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    # feature is 131951 rows
    # with 473 columns, 8 for the independent features, 465 for units
    #print features.head(10)
    #print "features is length ", len(features)
   
    # Values
    values = dataframe['ENTRIESn_hourly']
    m = len(values)

    # features now has 474 columns, we added one column for y intercept
    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    #print features.head(10)
    #print "features is length ", len(features)
   
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

    # Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to change this value
    num_iterations = 75 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    # print theta for the 8 feature values I used   
    print theta_gradient_descent[0:8]
    
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    # 
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed 
    # the 30 second limit on the compute servers.
    
    predictions = np.dot(features_array, theta_gradient_descent)
    return predictions, plot


def plot_cost_history(alpha, cost_history):
   """This function is for viewing the plot of your cost history.
   You can run it by uncommenting this

       plot_cost_history(alpha, cost_history) 

   call in predictions.
   
   If you want to run this locally, you should print the return value
   from this function.
   """
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )



file_path="C:/Users/dak/Documents/Udacity.IntroDataSciences/turnstile_data_master_with_weather.csv"    
turnstile = pandas.read_csv(file_path) 
#print turnstile.head(5)

####################################
# PREDICTIONS
####################################
myprediction, plot =  predictions(turnstile)
print plot
print "myprediction is length ", len(myprediction)
print myprediction

plt.figure() 
plt.ylabel('Predicted Entries')
plt.xlabel('Observed Entries')
plt.title('Predicted and observed values') 

y=myprediction
x=turnstile['ENTRIESn_hourly']

#slope, intercept = np.polyfit( turnstile['ENTRIESn_hourly'],myprediction, 1)
#line = (slope * turnstile['ENTRIESn_hourly']) + intercept
#plt.plot(line, turnstile['ENTRIESn_hourly'], 'b')

plt.scatter(x, y, c='r', alpha=0.5)
slope, intercept = np.polyfit( x, y, 1)
ys = (slope * x ) + intercept
plt.plot( x, ys )
x_axis = [-5000, 60000, -5000, 60000]
plt.axis(x_axis)
plt.show()




####################################
# residuals
####################################
print plot_residuals(turnstile, myprediction)

####################################
# r squared
####################################
myr2 = compute_r_squared(turnstile["ENTRIESn_hourly"], myprediction)
print "the r^2 value is: ", myr2

# fromt he class with a smaller set of the data
#Your r^2 value is 0.463968815042, for my first set of features
#Your r^2 value is 0.622087219608 for my seond set

