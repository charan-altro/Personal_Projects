import numpy as np
from scipy.optimize import newton
import datetime

# Helper function to compute the XIRR (only when applicable)
def xirr(cash_flows, dates, guess=0.1):
    def npv(rate):
        return sum([cf / (1 + rate) ** ((d - dates[0]).days / 365) for cf, d in zip(cash_flows, dates)])
    
    try:
        return newton(npv, guess, maxiter=100)
    except (RuntimeError, OverflowError):
        return None  # Return None if XIRR calculation fails

# Helper function to calculate the Average Monthly Rate
def average_monthly_rate(withdrawal):
    return (100000 - withdrawal) / 105000

# Helper function to calculate the Effective Interest Rate based on Average Monthly Rate
def effective_interest_rate(avg_monthly_rate):
    if avg_monthly_rate is None:
        return None
    return (1 + avg_monthly_rate) ** (12 / 21) - 1

# Generate dynamic dates for the 21 months
def generate_dates(start_date, months=21):
    return [start_date + datetime.timedelta(days=30 * i) for i in range(months)]
