# Stock Forecasting Project

A polished demo of a Python stock analysis and forecasting tool with both a command-line workflow and an interactive Streamlit dashboard.

![Project Dashboard](newplot.png)

## 🚀 Project Showcase

This repository demonstrates:

- Historical price retrieval for multiple stocks
- Technical indicator computation (SMA, RSI, volatility)
- Lightweight forecasting using naive and moving-average models
- Streamlit dashboard for interactive data visualization and export
- CSV export and reusable module structure for future extension

## 🌟 Features

- Fetch stock history for US symbols
- Compute technical indicators:
  - Simple moving averages (20 / 50)
  - RSI (14)
  - 20-day volatility
- Generate forecasts:
  - Naive forecast based on last close
  - Moving average forecast
- Interactive dashboard with Plotly charts and data export
- Easy symbol selection, period control, and forecast horizon tuning

## 📁 Project Structure

- `main.py` — entry point and analysis workflow
- `dashboard.py` — Streamlit app for visualization and export
- `data/` — data retrieval and source management
- `analysis/` — technical indicator and plotting helpers
- `models/` — forecasting utilities
- `utils/` — constants and file I/O helpers

## ⚡ Quick Start

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the command-line analysis for default stocks:

```bash
python main.py
```

4. Open the interactive dashboard:

```bash
streamlit run dashboard.py
```

## 🛠️ Usage Examples

Analyze specific symbols:

```bash
python main.py --symbols AAPL MSFT TSLA
```

Forecast the next 10 days:

```bash
python main.py --forecast-days 10
```

Save fetched data to CSV files:

```bash
python main.py --save-csv
```

## 📊 Dashboard Highlights

The Streamlit dashboard includes:

- **Price & Indicators** tab with closing price, SMA, and RSI charts
- **Forecasts** tab comparing naive and moving-average forecasts
- **Data Export** tab to download analyzed data as CSV

## 📦 Requirements

- Python 3.11+ recommended
- `pandas`
- `numpy`
- `matplotlib`
- `yfinance`
- `requests`
- `streamlit`
- `plotly`

## 💡 Extend the Project

- Add new data providers in `data/`
- Add more indicators in `analysis/indicators.py`
- Add advanced forecasting models in `models/forecast.py`
- Expand the dashboard with additional analytics and metrics

## 🔗 Notes

Use `newplot.png` as a GitHub preview image for the dashboard section.
