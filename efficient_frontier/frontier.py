import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Generate Synthetic Data
# ---------------------------------------------------------
# In a real scenario, we would download this using yfinance:
# data = yf.download(['AAPL', 'GOOG', 'MSFT', 'AMZN', 'TSLA'], start='2020-01-01')['Adj Close']

np.random.seed(42) # For reproducibility
num_days = 252 * 3 # 3 years of data
stocks = ['TECH', 'HLTH', 'ENER', 'FIN', 'CONS']

# Generate random returns (mean 0.05%, std dev 1.5% daily)
returns_data = np.random.normal(0.0005, 0.015, (num_days, len(stocks)))
df_returns = pd.DataFrame(returns_data, columns=stocks)

# ---------------------------------------------------------
# 2. Calculate Annualized Metrics
# ---------------------------------------------------------
mean_returns = df_returns.mean() * 252
cov_matrix = df_returns.cov() * 252

# ---------------------------------------------------------
# 3. Simulate Portfolios
# ---------------------------------------------------------
num_portfolios = 5000
results = np.zeros((3, num_portfolios)) # [Return, Volatility, Sharpe Ratio]

for i in range(num_portfolios):
    # Generate random weights
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights) # Normalize to sum to 1
    
    # Portfolio Return
    p_return = np.sum(mean_returns * weights)
    
    # Portfolio Volatility (Standard Deviation)
    # Formula: sqrt(w.T * Cov * w)
    p_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    
    # Store results
    results[0,i] = p_return
    results[1,i] = p_std_dev
    results[2,i] = results[0,i] / results[1,i] # Sharpe Ratio (assuming 0 risk-free rate for simplicity)

# ---------------------------------------------------------
# 4. Visualization
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.style.use('bmh') # Use a nice style

# Scatter plot colored by Sharpe Ratio
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis', marker='o', s=10, alpha=0.6)
plt.colorbar(label='Sharpe Ratio')

# Find the portfolio with the highest Sharpe Ratio
max_sharpe_idx = np.argmax(results[2,:])
max_sharpe_return = results[0, max_sharpe_idx]
max_sharpe_std = results[1, max_sharpe_idx]

# Mark the best portfolio
plt.scatter(max_sharpe_std, max_sharpe_return, c='red', s=100, edgecolors='black', label='Max Sharpe Ratio')

plt.title('Efficient Frontier Simulation (5,000 Portfolios)')
plt.xlabel('Expected Volatility (Risk)')
plt.ylabel('Expected Return')
plt.legend()
plt.grid(True, alpha=0.3)

print(f"Max Sharpe Ratio Portfolio:\nReturn: {max_sharpe_return:.2%}\nVolatility: {max_sharpe_std:.2%}")

# Save the plot instead of just showing it
plt.savefig('efficient_frontier_plot.png', dpi=300)
print("Graph saved as 'efficient_frontier_plot.png'")

