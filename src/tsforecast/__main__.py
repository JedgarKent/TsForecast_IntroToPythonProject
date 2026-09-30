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

    ts = TimeSeries.csv(args.file, args.date_col, args.value_col)
    train, test = ts.train_test_split(test_size=0.2)

    # 2. compare_models

    models = [NaiveForecaster(), MovingAverageForecaster(window_size=3)]
    results = compare_models(models, train.series, test.series)


    # 3. print results
    
    print(results)
    
    # 4. plot_forecast, save to outputs/

    horizon = len(test.series)
    for model in models:
        model.fit(train.series)
        predictions = model.predict(horizon)
        model_name = type(model).__name__
        save_path = f"output/{model_name}.png"
        plot_forecast(train.series, test.series, predictions, model_name, save_path)
        print(f"Saved plot to {save_path}")

    pass

if __name__ == "__main__":
    main()