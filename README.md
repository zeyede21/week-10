# 🛢️ Brent Oil Price Change Point Detection Dashboard

This project analyzes time series data of Brent oil prices using **Bayesian Change Point Detection** with `PyMC3`, and visualizes results using an interactive dashboard built with **Flask (Backend)** and **React (Frontend)**.

---

## 📌 Features

- Bayesian Change Point Detection (with PyMC3)
- Time series analysis (log returns, rolling statistics)
- Interactive dashboard with Flask + React
- Visual correlation of structural breaks with real-world events
- Modular code structure and clean data pipeline

---

## 📁 Project Structure



---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/zeyede21/week-10
cd brent-oil-change-point-dashboard

### 2. Create and activate virtual environment

conda create -n week-10 python=3.9.13
conda activate week-10

## 3. Install Python dependencies
pip install -r requirements.txt

#4. Start Flask backend
python app.py

## 5. Start React frontend
cd frontend
npm install
npm start

⚙️ Technologies Used
PyMC3 – Bayesian modeling

Pandas, NumPy, Matplotlib – Data analysis

Flask – Backend REST API

React.js – Frontend UI

ArviZ – Posterior diagnostics & visualization

🧪 Example Visuals
Rolling statistics and stationarity test (ADF)

Detected change points with confidence intervals

Historical events mapped to price structural changes


