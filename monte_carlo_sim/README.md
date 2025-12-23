# 🎲 Monte Carlo Risk Simulator

> *Quantifying uncertainty with Stochastic Calculus.*

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Simulation-013243?style=flat-square&logo=numpy&logoColor=white)
![Statistics](https://img.shields.io/badge/Math-Statistics-orange?style=flat-square)

## 🧐 Overview
Predicting a specific future stock price is impossible. Predicting a **probability distribution** of future prices is science. This project uses Monte Carlo simulations to model thousands of potential market scenarios, allowing us to calculate **Value at Risk (VaR)**—a standard metric in institutional risk management.

## ⚙️ Methodology
We model stock price evolution using **Geometric Brownian Motion (GBM)**:

$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

*   **Drift ($\mu$):** The expected return over time.
*   **Shock ($\sigma dW_t$):** Random volatility component.

## 📊 Visual Analysis

### 1. The Multiverse (1,000 Simulations)
![Monte Carlo Paths](monte_carlo_paths.png)
*   Each line represents one possible future timeline for the stock over the next year.
*   The spread of lines visualizes the cone of uncertainty.

### 2. Probability Distribution & VaR
![Final Price Distribution](monte_carlo_dist.png)
*   **Expected Value:** The peak of the bell curve ($108.40).
*   **Value at Risk (VaR):** The red dashed line ($76.52).
*   **Interpretation:** We can say with **95% confidence** that the portfolio value will not fall below $76.52.

## 🚀 Usage
```bash
# Navigate to directory
cd monte_carlo_sim

# Run the simulation
python monte_carlo.py
```
