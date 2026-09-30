# Time series forecast

A command-line tool for time series forecasting and model comparison.

Loads a time series from a CSV file, splits it into train/test sets,
fits simple forecasting models, compares their accuracy, and saves
forecast plots as images.

## Features

- Load TS data from CSV file
- Train/test split by time
- Two models:
  - NaiveForecaster — repeats the last known value
  - MovingAverageForecaster — uses the average of the last N values
- Compares models using MAE and RMSE
- Saves forecast plots to the `output/` folder

## Installation

Requires Python >= 3.10 and uv


git clone https://github.com/JedgarKent/TsForecast_IntroToPythonProject.git
cd TsForecast_IntroToPythonProject
uv pip install -e .


## Usage

uv run -m tsforecast --file data/aapl.csv --date-col Date --value-col Close --horizon 10

## Arguments
Argument         Required           Description
--file           Yes                Path to the input CSV file
--date-col       Yes                Name of the date column
--value-col      Yes                Name of the value column
--horizon        No                 Number of time periods to forecast

## Data

You can generate your data with:

uv run python -c "import yfinance as yf; df = yf.download('AAPL', start='2020-01-01', end='2024-01-01'); df.reset_index(inplace=True); df.to_csv('data/aapl.csv', index=False)"

## Project structure

src/tsforecast/
├── main.py # logic entry point
├── data.py # TimeSeries class: loading, splitting
├── forecast.py # Forecasting models (Naive, MovingAverage)
├── evaluation.py # Metrics (MAE, RMSE) and model comparison
└── viz.py # Plotting forecasts