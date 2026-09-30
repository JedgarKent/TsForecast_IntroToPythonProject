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

def compare_models(models, train_series, test_series):

    """Training each model on train_series and prediction on test_series. 
    Then computes MAE and RMSE for each model"""

    horizon = len(test_series)
    results = []

    for model in models:
        model.fit(train_series)
        predictions = model.predict(horizon)

        mae = mean_absolute_error(test_series, predictions)
        rmse = root_mean_squared_error(test_series, predictions)

        results.append({
            "model": type(model).__name__,
            "mae": mae,
            "rmse": rmse
        })

    return pd.DataFrame(results)