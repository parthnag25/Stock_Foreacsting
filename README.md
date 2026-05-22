# Stock Forecasting Portfolio Project

A portfolio-ready Python application that demonstrates stock analytics, technical indicators, forecasting, and interactive visualization using Streamlit.

![Project Dashboard](newplot.png)

## Business Problem

Investors and analysts need a fast way to understand stock momentum, risk, and short-term outlooks using historical price data. This project solves that problem by combining data retrieval, technical analysis, and simple forecasting models into a single interactive dashboard.

## Live Demo

This repository is ready to deploy on Streamlit Community Cloud. Once deployed, visitors can explore:

- stock price history and moving averages
- RSI and volatility metrics
- forecast comparisons between naive and moving average models
- downloadable CSV export of the analysis data

See `STREAMLIT_DEPLOYMENT.md` for deployment instructions.

## Key Features

- Historical price retrieval for U.S. stocks using `yfinance`
- Technical indicators:
  - 20-day and 50-day moving averages
  - 14-day RSI
  - annualized 20-day volatility
- Forecasting models:
  - naive persistence forecast
  - moving-average forecast
- Interactive Streamlit dashboard with charts, metrics, and export functionality
- CSV export support for analyzed price data

## Tech Stack

- Python 3.11+
- pandas
- numpy
- matplotlib
- yfinance
- streamlit
- plotly
- GitHub Actions for CI

## Project Structure

- `main.py` — command-line analysis workflow
- `dashboard.py` — Streamlit dashboard app
- `data/` — historical price fetcher and source configuration
- `analysis/` — technical indicator and visualization helpers
- `models/` — forecasting algorithm implementations
- `utils/` — constants and CSV file helpers
- `assets/` — dashboard screenshots and architecture diagrams
- `tests/` — basic automated tests
- `.github/workflows/` — CI automation

## Results and Insights

This project provides:

- a clear signal of stock direction using moving averages
- overbought/oversold RSI insights for momentum assessment
- volatility measurement for risk awareness
- a quick visual comparison of forecast scenarios

## Limitations

- Forecasts are intentionally simple and not production-grade
- Only one data source is fully supported (`yahoo`)
- No backtesting or forecast validation metrics are currently included
- Models do not account for macroeconomic factors or corporate events

## Future Improvements

- add more advanced forecasting models such as ARIMA or Prophet
- implement backtesting and model performance metrics
- support additional data sources beyond Yahoo Finance
- add portfolio-level analytics and multi-stock comparison
- include automated tests and GitHub Actions coverage reporting

## 🚀 Run the project

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the command-line analysis:

```bash
python main.py
```

4. Launch the dashboard:

```bash
streamlit run dashboard.py
```

## Example usage

Analyze specific stocks:

```bash
python main.py --symbols AAPL MSFT TSLA
```

Run a 10-day forecast:

```bash
python main.py --forecast-days 10
```

Export analyzed data:

```bash
python main.py --save-csv
```

## What the dashboard shows

- Price chart with SMA 20 and SMA 50
- RSI trend and overbought/oversold thresholds
- forecast visualization for naive and moving-average models
- data export for downstream analysis

## Requirements

- Python 3.11+
- pandas
- numpy
- matplotlib
- yfinance
- requests
- streamlit
- plotly
