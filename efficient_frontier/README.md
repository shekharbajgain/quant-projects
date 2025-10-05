# Efficient Frontier Visualizer 📈

## The "Why"
I kept hearing the term "diversification" in my finance classes, but it always felt like a buzzword. "Don't put all your eggs in one basket"—sure, I get it. But *mathematically*, why does it work?

I wanted to see it with my own eyes. I wanted to prove that you can actually **lower** your risk while keeping the same return, just by mixing assets.

## The Process
I started by generating some fake stock data (because I didn't want to pay for a Bloomberg terminal yet!). I created 5 imaginary stocks:
*   **TECH** (High risk, high reward)
*   **HLTH** (Steady)
*   **ENER** (Volatile)
*   **FIN** (Cyclical)
*   **CONS** (Safe)

Then came the heavy lifting. I used `numpy` to simulate **5,000 different portfolios**. Each dot on the graph represents a unique combination of these stocks.

### The Hard Part 😅
My first attempt was a disaster. I tried to run 1,000,000 simulations and my laptop fan sounded like a jet engine taking off. I realized that brute force isn't always the answer. I scaled it back to 5,000, which was enough to see the curve without melting my CPU.

## The Result
![Efficient Frontier Graph](efficient_frontier_plot.png)

Look at that curve! It's beautiful.
*   The **yellow dots** are the best portfolios (High Sharpe Ratio).
*   The **purple dots** are the worst (High risk, low return).

**My "Aha!" Moment:**
See how the curve bends backward? That means there are portfolios that have *less* risk than the safest single stock. That blew my mind. Math is cool.

## How to Run It
```bash
pip install -r ../requirements.txt
python frontier.py
```
