Interactive SIP Calculator (Matplotlib and ipywidgets)

Estimate the future value of a Systematic Investment Plan (SIP) with live, interactive sliders. Built for Jupyter Notebook/JupyterLab using Matplotlib for visualization and ipywidgets for controls.

TL;DR: Tweak monthly SIP, duration, and rate range; watch the payoff curve update in real time.


✨ Features

Interactive Sliders: Monthly SIP, investment duration (years), and interest-rate range.

Real-time Plot Updates: Immediate feedback as you adjust parameters.

Clear Visualization: See how returns evolve across rates.

Lightweight: Minimal deps; runs smoothly in Jupyter.

Educational: Great for students, finance enthusiasts, and quick prototyping.

🧠 How It Works

We compute SIP future value (FV) using monthly compounding. For a monthly contribution P, annual rate R (as decimal), and Y years:

Monthly rate: i = R / 12

Number of months: n = 12 * Y

FV formula:FV = P * [ ((1 + i)^n - 1) / i ] * (1 + i)
