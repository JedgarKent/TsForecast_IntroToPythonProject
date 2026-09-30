import pandas as pd

class NaiveForecaster:

    ## Prediction by using the last observation of given value

    def fit(self, train_series):
        self.last_value = train_series.iloc[-1]
        return self

    def predict(self, periods):
        return [self.last_value] * periods

class MovingAverageForecaster:
    
    ## Prediction by computing the mean of the last window_size observations of train_series
    
    def __init__(self, window_size=3):
        self.window_size = window_size

    def fit(self, train_series):
        last_values = train_series.tail(self.window_size)
        self.average = last_values.mean()
        return self