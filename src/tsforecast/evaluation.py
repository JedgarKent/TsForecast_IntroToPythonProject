"""Adding metrics for evaluation of TSforecast models"""

import pandas as pd

def mean_absolute_error(y_true, y_pred):

    """Mean Absolute Error (MAE) 
    
    y true and y predicted are lists or pandas series of the same length"""

    errors = []
    for i, k in zip(y_true, y_pred):
        errors.append(abs(i-k))
    return sum(errors)/len(errors)

def root_mean_squared_error(y_true, y_pred):

    """Same as MAE but with squared errors (RMSE)
    
     y true and y predicted are lists or pandas series of the same length"""

    sq_errors = []
    for i, k in zip(y_true, y_pred):
        sq_errors.append((i-k)**2)
    mean_squared =  sum(sq_errors)/len(sq_errors)
    return mean_squared ** 0.5