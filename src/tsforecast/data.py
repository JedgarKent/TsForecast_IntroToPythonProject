### Loading and preprocessing data for TS analysis

import pandas as pd

class TimeSeries:
    def __init__(self, series: pd.Series, name: str = "Time Series"):
        self.series = series
        self.name = name

    @classmethod
    def csv(cls, path: str, date_col: str, value_col: str):
        df = pd.read_csv(path, parse_dates = [date_col])
        df = df.set_index(date_col).sort_index()
        return cls(df[value_col], name=value_col)

    def __len__(self):
        return len(self.series)