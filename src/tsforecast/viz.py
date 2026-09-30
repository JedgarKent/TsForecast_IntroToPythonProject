"""Plotting for forecasting models and model comparison"""

import matplotlib.pyplot as plt

def plot_forecast(train_series, test_series, predictions, model_name, save_path):
   
    """Plotting the train_series, test_series and predictions of a model on the same graph
    train_series, test_series - pandas series with the dates (historic part)
    predictions - list or pandas series with the predicted values (future part)
    model_name - string with the name of the model (for title of the plot)
    save_path - path to save the plot"""

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(train_series.index, train_series.values, label="Train (history)")
    ax.plot(test_series.index, test_series.values, label="Test (actual)")
    ax.plot(test_series.index, predictions, label=f"Forecast ({model_name})", linestyle="--")

    ax.set_title(f"Forecast vs Actual — {model_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()

    fig.savefig(save_path)
    plt.close(fig)

