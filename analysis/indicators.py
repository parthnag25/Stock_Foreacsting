import pandas as pd


def moving_average(series: pd.Series, window: int = 20) -> pd.Series:
    return series.rolling(window=window, min_periods=1).mean()


def volatility(series: pd.Series, window: int = 20) -> pd.Series:
    return series.pct_change().rolling(window=window, min_periods=1).std() * (252 ** 0.5)


def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss.replace(0, 1e-9)
    return 100 - (100 / (1 + rs))


def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["SMA_20"] = moving_average(result["Close"], window=20)
    result["SMA_50"] = moving_average(result["Close"], window=50)
    result["Volatility_20"] = volatility(result["Close"], window=20)
    result["RSI_14"] = rsi(result["Close"], window=14)
    return result
