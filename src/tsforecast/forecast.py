import pandas as pd

class NaiveForecaster:
    def fit(self, train_series):
        self.last_value = train_series.iloc[-1]
        return self

    def predict(self, periods):
        return [self.last_value] * periods