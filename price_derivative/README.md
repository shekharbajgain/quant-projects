# Price Derivative Analyzer 📉➡️📈

## The "Why"
I struggled with Calculus I. Derivatives felt abstract. "The slope of the tangent line"—who cares?

Then I started getting into trading. I noticed that sometimes a stock price is still going up, but it feels "tired." It's running out of steam. I realized: **That's just negative acceleration!**

I built this tool to prove that Calculus isn't just for engineers—it's for traders too.

## The Process
I created a synthetic stock price that moves in a wave. Then, I used `pandas` to calculate:
1.  **Velocity (1st Derivative):** How fast is the price changing? ($/day)
2.  **Acceleration (2nd Derivative):** Is the speed increasing or decreasing? ($/day²)

### The Surprise 😲
I expected the acceleration to just follow the price. But look at the graph below.

## The Result
![Derivative Analysis Graph](derivative_analysis_plot.png)

**The Purple Line (Acceleration) is the key.**
Notice how the purple line crosses zero and goes negative *before* the blue line (Price) actually peaks?

*   **Price** is what happened.
*   **Velocity** is what is happening.
*   **Acceleration** is what *will* happen.

This project taught me that math is a predictive tool, not just a descriptive one.

## How to Run It
```bash
pip install -r ../requirements.txt
python derivative_analysis.py
```
