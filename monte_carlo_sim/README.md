# Monte Carlo Risk Simulator 🎲

## The "Why"
"Where will Apple stock be in a year?"
If anyone gives you a specific number, they are lying. The future is random.

But I learned that while you can't predict the *exact* price, you can predict the *probability* of a price. That's what Monte Carlo simulations do. It's like Dr. Strange looking at 14 million possible futures.

## The Process
I used a model called **Geometric Brownian Motion**. It sounds fancy, but it just means:
*   **Drift:** The stock generally goes up over time (hopefully).
*   **Shock:** Every day, something random happens (news, earnings, tweets).

I wrote a Python script to simulate 1,000 different "timelines" for a single stock over the next year.

### The Hard Part 🤯
Understanding the math was tough. `exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)`. I stared at that formula for 3 days. But once I broke it down into "Drift" vs "Randomness", it clicked.

## The Result

### The 1,000 Futures
![Monte Carlo Paths](monte_carlo_paths.png)
This mess of lines represents uncertainty. Most paths go up, but some crash. This is reality.

### The Distribution
![Final Price Distribution](monte_carlo_dist.png)
This is the money shot.
*   **Mean:** $108.40 (The most likely outcome).
*   **VaR (Value at Risk):** $76.52. This tells me: "In the worst 5% of cases, I will lose this much money."

This project changed how I view risk. It's not a feeling; it's a number.

## How to Run It
```bash
pip install -r ../requirements.txt
python monte_carlo.py
```
