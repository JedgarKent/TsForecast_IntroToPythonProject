""""Adding metrics for evaluation of TSforecast models"""""

import pandas as pd

def mean_absolute_error(y_true, y_pred):

    """"Mean Absolute Error (MAE) 
    
    y true and y predicted are lists or pandas series of the same length"""

    errors = []
    for i, k in zip(y_true, y_pred):
        errors.append(abs(i-k))
    return sum(errors)/len(errors)
