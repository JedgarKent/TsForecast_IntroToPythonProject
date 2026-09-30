"""Command-line interface for tsforecast."""

import argparse

from tsforecast.data import TimeSeries
from tsforecast.forecast import NaiveForecaster, MovingAverageForecaster
from tsforecast.evaluation import compare_models
from tsforecast.viz import plot_forecast


def main():
    parser = argparse.ArgumentParser(prog="tsforecast")
    parser.add_argument("--file", required=True, help="path to CSV file")
    parser.add_argument("--date-col", required=True)
    parser.add_argument("--value-col", required=True)
    parser.add_argument("--horizon", type=int, default=10)
    args = parser.parse_args()

    # 1. load data
    # 2. train_test_split
    # 3. compare_models
    # 4. print results
    # 5. plot_forecast, save to outputs/
    pass

if __name__ == "__main__":
    main()