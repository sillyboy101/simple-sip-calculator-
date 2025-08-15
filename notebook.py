import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider, FloatRangeSlider

def calculate_sip_fv(sip, years, rate_min, rate_max):
    rates = np.arange(rate_min, rate_max + 0.1, 0.1)
    n = int(years * 12)
    fv = []
    for r in rates:
        monthly_rate = r / 12 / 100
        future_value = sip * (((1 + monthly_rate) ** n - 1) / monthly_rate) * (1 + monthly_rate)
        fv.append(future_value)
    return rates, fv

def plot_sip(sip=10000, years=10, rate_range=(6, 12)):
    rate_min, rate_max = rate_range
    rates, fvs = calculate_sip_fv(sip, years, rate_min, rate_max)
    plt.figure(figsize=(8,5))
    plt.plot(rates, fvs, marker='o', color='steelblue')
    plt.fill_between(rates, fvs, color='steelblue', alpha=0.2)
    plt.title("Future Value of SIP vs. Interest Rate")
    plt.xlabel("Interest Rate (%)")
    plt.ylabel("Future Value (₹)")
    plt.grid(True)
    plt.show()

# Use ipywidgets for interactive sliders
interact(
    plot_sip,
    sip=IntSlider(min=1000, max=50000, step=1000, value=10000, description="SIP Amount (₹)"),
    years=IntSlider(min=1, max=30, step=1, value=10, description="Duration (Years)"),
    rate_range=FloatRangeSlider(value=[6,12], min=3, max=20, step=0.5, description="Interest Range (%)")
)
