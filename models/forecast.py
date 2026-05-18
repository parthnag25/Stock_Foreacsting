import pandas as pd


def naive_forecast(df: pd.DataFrame, days: int = 5) -> pd.DataFrame:
    last_price = df["Close"].iloc[-1]
    start_date = pd.to_datetime(df["Date"].iloc[-1]) + pd.Timedelta(days=1)
    future_dates = pd.date_range(start=start_date, periods=days, freq="B")
    return pd.DataFrame({"Date": future_dates, "Forecast": [last_price] * days})


def moving_average_forecast(df: pd.DataFrame, window: int = 5, days: int = 5) -> pd.DataFrame:
    last_ma = df["Close"].rolling(window=window, min_periods=1).mean().iloc[-1]
    start_date = pd.to_datetime(df["Date"].iloc[-1]) + pd.Timedelta(days=1)
    future_dates = pd.date_range(start=start_date, periods=days, freq="B")
    return pd.DataFrame({"Date": future_dates, "Forecast": [last_ma] * days})
