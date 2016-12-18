#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = np.absolute(predictions - net_worths).flatten()

    fullsize = len(predictions)
    newSize = fullsize*0.9

    minIndexes = error.argsort()[0:int(newSize - 1)]
    cleaned_data = [(ages[i], net_worths[i], error[i]) for i in minIndexes]

    return cleaned_data

