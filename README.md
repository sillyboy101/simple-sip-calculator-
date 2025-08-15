# Interactive SIP Calculator

An interactive Jupyter Notebook tool to estimate the future value of a **Systematic Investment Plan (SIP)** with variable interest rates.  
Built with **Matplotlib** for visualization and **ipywidgets** for interactive controls.

## Features

- **Interactive sliders** to adjust:
  - Monthly SIP amount
  - Investment duration (years)
  - Interest rate range
- **Real-time plot updates** as parameters change
- **Clear visualization** of investment growth
- **Lightweight**: minimal dependencies, works in Jupyter Notebook/Lab
- **Educational**: useful for learning SIP concepts and scenarios

## How It Works

The calculator uses the **future value of SIP formula** with monthly compounding:FV = P * [ ((1 + i)^n - 1) / i ] * (1 + i)


Where:
- `P` = monthly investment
- `i` = monthly interest rate (annual rate / 12)
- `n` = total number of months

The tool computes FV across a user-defined interest rate range and plots the results interactively.

## Installation

```bash
# Create and activate virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install jupyterlab matplotlib ipywidgets numpy


