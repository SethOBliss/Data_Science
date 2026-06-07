# USD/INR Exchange Rate Forecasting with ARIMA & SARIMA

> Time series forecasting of the US Dollar to Indian Rupee exchange rate using classical statistical models — built as part of coursework at Hindu College, University of Delhi.

---

## Overview

This project builds and evaluates an **ARIMA/SARIMA pipeline** to forecast daily USD/INR exchange rates. The goal was to understand the temporal structure of currency data and produce short-horizon forecasts, assessed against held-out test data using Mean Absolute Error (MAE).

| Model                    | Order                  | MAE (Test Set) |
|--------------------------|------------------------|----------------|
| ARIMA                    | (1, 1, 1)              | 5.5754 INR     |
| **SARIMA** ✓ *(winner)*  | (1,1,1)(1,1,1,5)       | **1.2041 INR** |

---

## Methodology

### 1. Data Collection
- **Source:** Yahoo Finance via the `yfinance` Python library
- **Ticker:** `INR=X` (USD/INR daily closing price)
- **Period:** Dec 2003 – Sep 2023 (~20 years of daily data)
- **Frequency:** Daily

### 2. Preprocessing & Visualisation
- Plotted the raw time series to inspect trends and seasonality
- Computed rolling mean and standard deviation to visually assess stationarity

### 3. Stationarity Testing
- Applied the **Augmented Dickey-Fuller (ADF) test** to check for unit roots
- Applied first-order differencing where the series was found to be non-stationary
- Re-tested post-differencing to confirm stationarity

### 4. Model Identification
- Plotted **ACF** (Autocorrelation Function) and **PACF** (Partial Autocorrelation Function) to identify candidate AR and MA orders
- Used **AIC/BIC** criteria to compare model configurations and select optimal parameters

### 5. Model Fitting
- **ARIMA(p, d, q):** `ARIMA(1, 1, 1)`
- **SARIMA(p, d, q)(P, D, Q, s):** `SARIMA(1,1,1)(1,1,1,5)` — seasonal period of 5 trading days
- Fitted both models using `statsmodels`

### 6. Evaluation
- Split data into **train / test** sets (80/20)
- Generated forecasts on the test window
- Evaluated using **Mean Absolute Error (MAE)**
- Compared ARIMA vs SARIMA forecast accuracy

---

## Results

Both models confirmed that the USD/INR series is non-stationary in levels but stationary after first differencing (d=1). SARIMA(1,1,1)(1,1,1,5) substantially outperformed the baseline ARIMA(1,1,1), reducing MAE from **5.5754 to 1.2041 INR** — a ~78% improvement — demonstrating that weekly seasonality (5 trading days) is a significant driver of short-term exchange rate movements. The strong seasonal component suggests that day-of-week effects in trading volume and liquidity play a meaningful role in USD/INR dynamics over a 20-year horizon.

---

## Tech Stack

| Library       | Purpose                          |
|---------------|----------------------------------|
| `yfinance`    | Data download from Yahoo Finance |
| `pandas`      | Data manipulation                |
| `matplotlib`  | Time series visualisation        |
| `statsmodels` | ARIMA / SARIMA modelling         |
| `sklearn`     | MAE evaluation                   |

---

## Repository Structure

```
Python-Repo/
│
├── Prediction_Model.py       # Core modelling script
├── X.csv                     # Dataset (USD/INR closing prices)
└── README.md                 # This file
```

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/SethOBliss/Python-Repo.git
cd Python-Repo

# 2. Install dependencies
pip install yfinance pandas matplotlib statsmodels scikit-learn

# 3. Run the script
python Prediction_Model.py
```

---

## Author

**Ayush Seth**
B.Sc. (Hons.) Statistics, Hindu College, University of Delhi
[linkedin.com/in/sethayush](https://linkedin.com/in/sethayush) | sethayush1466@gmail.com
