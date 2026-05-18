import os

import pandas as pd


def save_prices_to_csv(df: pd.DataFrame, folder: str, symbol: str) -> str:
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{symbol}.csv")
    df.to_csv(path, index=False)
    return path


def load_prices_from_csv(folder: str, symbol: str) -> pd.DataFrame:
    path = os.path.join(folder, f"{symbol}.csv")
    return pd.read_csv(path)
