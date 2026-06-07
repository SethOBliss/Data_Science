# USD/INR Exchange Rate Forecasting with ARIMA & SARIMA

> Time series forecasting of the US Dollar to Indian Rupee exchange rate using classical statistical models — built as part of coursework at Hindu College, University of Delhi.

---

## Overview

This project builds and evaluates an **ARIMA/SARIMA pipeline** to forecast daily USD/INR exchange rates. The goal was to understand the temporal structure of currency data and produce short-horizon forecasts, assessed against held-out test data using Mean Absolute Error (MAE).

| Model  | MAE (Test Set) |
|--------|---------------|
| ARIMA  | `[fill in]`   |
| SARIMA | `[fill in]`   |

---

## Methodology

### 1. Data Collection
- **Source:** Yahoo Finance via the `yfinance` Python library
- **Ticker:** `INR=X` (USD/INR daily closing price)
- **Period:** `[fill in — e.g., Jan 2018 to Sep 2023]`
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
- **ARIMA(p, d, q):** `[fill in final parameters, e.g., ARIMA(1,1,1)]`
- **SARIMA(p, d, q)(P, D, Q, s):** `[fill in final parameters]`
- Fitted both models using `statsmodels`

### 6. Evaluation
- Split data into **train / test** sets (`[fill in split ratio, e.g., 80/20]`)
- Generated forecasts on the test window
- Evaluated using **Mean Absolute Error (MAE)**
- Compared ARIMA vs SARIMA forecast accuracy

---

## Results

`[Add a brief 2–3 line summary of what you found — e.g., which model performed better, whether seasonality was significant, any interesting patterns in the residuals.]`

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
