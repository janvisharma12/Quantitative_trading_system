# 📈 Quantitative Trading System — NIFTY 50 (5-Minute Frequency)

## 🔍 Project Overview
This project implements a **complete end-to-end quantitative trading system** for the Indian derivatives market using **NIFTY 50 spot, futures, and options data** at a **5-minute frequency**.

The objective is to demonstrate strong capabilities across:
- Financial data engineering
- Feature engineering
- Market regime detection
- Algorithmic trading strategy design
- Machine learning modeling
- Statistical and outlier analysis
- Modular, production-ready Python architecture

The system is designed to be **reproducible, extensible, and interview-ready**.

---

## 🧠 Key Highlights
- 📊 **1 year of high-frequency (5-minute) NIFTY data**
- 🔁 **Automatic futures rollover handling**
- 🎯 **Options chain modeling (ATM ±2 strikes, CE & PE)**
- 📉 **Market regime detection (trend / volatility regimes)**
- 🤖 **Machine learning-based return prediction**
- 🧪 **Robust statistical & outlier analysis**
- 🧱 **Clean separation of notebooks and production code**

---

## 🗂 Repository Structure
```
├── data/ # Raw & processed CSV datasets
├── notebooks/ # Research & analysis notebooks
│ ├── 01_data_acquisition.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_regime_detection.ipynb
│ ├── 05_baseline_strategy.ipynb
│ ├── 06_ml_models.ipynb
│ └── 07_outlier_analysis.ipynb
├── src/ # Production-ready Python modules
│ ├── data_utils.py
│ ├── features.py
│ ├── greeks.py
│ ├── regime.py
│ ├── strategy.py
│ ├── backtest.py
│ └── ml_models.py
├── models/ # Saved ML models
├── results/ # Strategy metrics & outputs
├── plots/ # Visualizations
├── requirements.txt
└── README.md
```

---

## 📦 Data Description

### 1️⃣ NIFTY 50 Spot
- Interval: **5 minutes**
- Fields: `OHLCV`
- Source: **NSE Historical Data**

### 2️⃣ NIFTY Futures
- Instrument: **Current month FUTIDX**
- Automatic **monthly rollover**
- Fields: `OHLCV`, `Open Interest`

### 3️⃣ NIFTY Options
- Strikes: **ATM, ATM ±1, ATM ±2**
- Contracts: **Call (CE) & Put (PE)**
- Fields:
  - Last Traded Price (LTP)
  - Implied Volatility (IV)
  - Open Interest
  - Volume

---

## 🧩 Project Workflow

### 🔹 Task 1 — Data Engineering
- Fetching high-frequency spot, futures, and options data
- Time alignment and trading-hour filtering
- Handling missing bars and bad ticks
- Futures rollover logic

### 🔹 Task 2 — Feature Engineering
- Returns & log-returns
- Volatility measures
- Trend & momentum indicators
- Rolling statistics
- Options-based features (IV, OI dynamics)

### 🔹 Task 3 — Market Regime Detection
- Identification of market regimes using statistical & ML techniques
- Volatility-based and trend-based regime labeling
- Regime-aware feature augmentation

### 🔹 Task 4 — Baseline Trading Strategies
- Rule-based benchmark strategies
- Regime-conditioned trading logic
- Position sizing and risk constraints
- Performance metrics:
  - CAGR
  - Sharpe Ratio
  - Max Drawdown
  - Win rate

### 🔹 Task 5 — Machine Learning Models
- Supervised ML models for return/direction prediction
- Feature selection and validation
- Train/validation/test split respecting time series constraints
- Model persistence for reproducibility

### 🔹 Task 6 — Outlier & Statistical Analysis
- Return distribution analysis
- Extreme event detection
- Drawdown behavior
- Strategy robustness evaluation

---

## 📊 Results & Evaluation
All strategy outputs, metrics, and plots are stored in:
- `results/`
- `plots/`

Each strategy is evaluated on:
- Absolute returns
- Risk-adjusted performance
- Stability across market regimes

---

## 🛠 Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn**
- **NSE Historical Data**
- **Jupyter Notebook**

---

## 🚀 How to Run
```bash
git clone <repository-url>
cd quantitative-trading-system
pip install -r requirements.txt
```

Then run notebooks sequentially:
notebooks/01_data_acquisition.ipynb
→
notebooks/07_outlier_analysis.ipynb
