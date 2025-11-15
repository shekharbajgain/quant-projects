import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Generate Synthetic Price Data
# ---------------------------------------------------------
# Creating a price that looks like a stock: Trend + Sine Wave + Noise
np.random.seed(101)
days = np.arange(200)
trend = days * 0.1
cycle = 10 * np.sin(days / 10)
noise = np.random.normal(0, 2, 200)

price = 100 + trend + cycle + noise
dates = pd.date_range(start='2023-01-01', periods=200)

df = pd.DataFrame({'Price': price}, index=dates)

# ---------------------------------------------------------
# 2. Calculate Derivatives (Calculus in Action)
# ---------------------------------------------------------
# Smooth the data first to reduce noise impact on derivatives
df['MA_10'] = df['Price'].rolling(window=10).mean()

# First Derivative: Velocity (Rate of Change)
# How fast is the price changing? ($ per day)
df['Velocity'] = df['MA_10'].diff()

# Second Derivative: Acceleration (Rate of Change of Velocity)
# Is the trend speeding up or slowing down?
df['Acceleration'] = df['Velocity'].diff()

# ---------------------------------------------------------
# 3. Visualization
# ---------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Plot 1: Price
ax1.plot(df.index, df['Price'], label='Raw Price', alpha=0.5, color='gray')
ax1.plot(df.index, df['MA_10'], label='Smoothed Price (MA 10)', color='blue', linewidth=2)
ax1.set_title('Stock Price (f(x))')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Velocity (1st Derivative)
ax2.plot(df.index, df['Velocity'], color='orange', label='Velocity (f\'(x))')
ax2.axhline(0, color='black', linestyle='--', alpha=0.5) # Zero line
ax2.set_title('Velocity: Momentum (Rate of Change)')
ax2.set_ylabel('$ / Day')
ax2.grid(True, alpha=0.3)

# Plot 3: Acceleration (2nd Derivative)
ax3.plot(df.index, df['Acceleration'], color='purple', label='Acceleration (f\'\'(x))')
ax3.axhline(0, color='black', linestyle='--', alpha=0.5)
ax3.set_title('Acceleration: Change in Momentum')
ax3.set_ylabel('$ / Day^2')
ax3.grid(True, alpha=0.3)

# Highlight a point where acceleration turns negative (Trend slowing down)
# This often happens before the price actually peaks
plt.xlabel('Date')
plt.tight_layout()

print("Analysis Complete.")
print("Notice how Acceleration (Purple) often crosses zero BEFORE the Price (Blue) peaks.")
print("This is the predictive power of Calculus applied to markets.")

# Save the plot
plt.savefig('derivative_analysis_plot.png', dpi=300)
print("Graph saved as 'derivative_analysis_plot.png'")

