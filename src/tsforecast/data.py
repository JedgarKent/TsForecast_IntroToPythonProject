### Loading and preprocessing data for TS analysis

import pandas as pd
import matplotlib.pyplot as plt

class TimeSeries:
    def __init__(self, series: pd.Series, name: str = "Time Series"):
        self.series = series
        self.name = name

    def csv(self, path, date_col, value_col):
        df = pd.read_csv(path, parse_dates = [date_col])
        df = df.set_index(date_col).sort_index()
        return self(df[value_col], name=value_col)
    
    def train_test_split(self, test_size=0.2):
        index_for_split = int(len(self.series)) * (1 - test_size)
        train_series = self.series.iloc[:index_for_split]
        test_series = self.series.iloc[index_for_split:]
        return TimeSeries(train_series, name = self.name + " (train)"), TimeSeries(test_series, name = self.name + " (test)")

    def plot(self):
        plt.figure(figsize = (10, 6))
        plt.plot(self.series, label = self.name)
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title(self.name)
        plt.show()

    def __len__(self):
            return len(self.series)