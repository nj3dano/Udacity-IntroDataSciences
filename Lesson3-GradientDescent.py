import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    
    cost_history = []

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    
    # m is how many data points, so this is equal to the length of values
    # remember in python to make floats so division works
    m = len(values) * 1.0
    alpha = alpha * 1.0
    
    # If you do need to iterate over a sequence of numbers,
    # the built-in function range() comes in handy
    for i in range(num_iterations):
        
        # call the cost function
        cost_history.append( (compute_cost(features, values, theta)) )
                
        # In this exercise, output data points (or the Y's) are represented by 'values'
        # and the input data points (or the X's) are represented by 'features'.
         
        # J(Theta) is the cost function
         
        # "theta" is a vector of coefficient values
         
        # m - how many data points
         
        # cost history tracks how cost evolves over iterations
         
        # This is the predicted values
        # numpy.dot(features, theta) takes each row of features 
        # (representing the features associated with a single data point)
        # and computes the sum of the element-wise product between
        # feature values and thetas for creating the predictions vector.
         
        # matrix multiplication (Numpy.dot) will be doing the summation
        
        # Y is values, observed values
        # hXi is summation of theta across features, predicted value of Y^i
        Y = values
        hXi = numpy.dot(features, theta)
        mySummation = numpy.dot( (Y - hXi), features )
        theta = theta + ((alpha/m) * (mySummation))
    
    #Theta =  [45.35759233  -9.02442042  13.69229668]
    return theta, pandas.Series(cost_history) # leave this line for the grader


