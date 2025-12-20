import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Parameters
# ---------------------------------------------------------
S0 = 100      # Initial Stock Price
mu = 0.08     # Expected Annual Return (Drift)
sigma = 0.20  # Annual Volatility (Standard Deviation)
T = 1.0       # Time horizon in years
dt = 1/252    # Time step (1 trading day)
N = 252       # Number of time steps (days)
simulations = 1000 # Number of paths to simulate

# ---------------------------------------------------------
# 2. Monte Carlo Simulation (Geometric Brownian Motion)
# ---------------------------------------------------------
# Formula: S_t = S_{t-1} * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)
# Where Z is a standard normal random variable

np.random.seed(42)

# Create a matrix to hold all price paths
# Rows = Time steps, Columns = Simulations
price_paths = np.zeros((N + 1, simulations))
price_paths[0] = S0

for t in range(1, N + 1):
    # Generate random shocks (Z) for all simulations at once
    Z = np.random.standard_normal(simulations)
    
    # Calculate the change factor
    drift = (mu - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt) * Z
    
    # Update prices
    price_paths[t] = price_paths[t-1] * np.exp(drift + diffusion)

# ---------------------------------------------------------
# 3. Analysis
# ---------------------------------------------------------
final_prices = price_paths[-1]
mean_final_price = np.mean(final_prices)
var_95 = np.percentile(final_prices, 5) # 5th percentile (95% Value at Risk level)

print(f"Simulation Results ({simulations} paths):")
print(f"Start Price: ${S0}")
print(f"Expected Mean Final Price: ${mean_final_price:.2f}")
print(f"95% Worst Case (VaR): ${var_95:.2f}")

# ---------------------------------------------------------
# 4. Visualization
# ---------------------------------------------------------
plt.figure(figsize=(12, 6))

# Plot the first 50 paths to avoid clutter
plt.plot(price_paths[:, :50], alpha=0.4, linewidth=1)

# Plot the mean path
plt.plot(np.mean(price_paths, axis=1), color='black', linewidth=3, linestyle='--', label='Mean Path')

plt.title(f'Monte Carlo Simulation: Geometric Brownian Motion ({simulations} runs)')
plt.xlabel('Trading Days')
plt.ylabel('Stock Price ($)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('monte_carlo_paths.png', dpi=300)
print("Paths graph saved as 'monte_carlo_paths.png'")

# Histogram of final prices
plt.figure(figsize=(10, 5))
plt.hist(final_prices, bins=50, color='skyblue', edgecolor='black')
plt.axvline(mean_final_price, color='red', linestyle='dashed', linewidth=2, label=f'Mean: ${mean_final_price:.2f}')
plt.axvline(var_95, color='orange', linestyle='dashed', linewidth=2, label=f'5% VaR: ${var_95:.2f}')
plt.title('Distribution of Final Stock Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('monte_carlo_dist.png', dpi=300)
print("Distribution graph saved as 'monte_carlo_dist.png'")

