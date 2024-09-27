import numpy as np
from scipy.optimize import newton

# Helper function to compute the XIRR
def xirr(cash_flows, dates):
    def npv(rate):
        return sum([cf / (1 + rate) ** ((d - dates[0]).days / 365) for cf, d in zip(cash_flows, dates)])
    
    return newton(npv, 0.1)

# Helper function to calculate the effective interest rate
def effective_interest_rate(monthly_rate):
    return (1 + monthly_rate) ** 12 - 1

# Example cash flow data and dates
cash_flows = [
    85000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 
    -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000
]

# Corresponding dates (in the same order as the cash flows)
import datetime
dates = [
    datetime.datetime(2023, 7, 10),
    datetime.datetime(2023, 8, 10),
    datetime.datetime(2023, 9, 10),
    datetime.datetime(2023, 10, 10),
    datetime.datetime(2023, 11, 10),
    datetime.datetime(2023, 12, 10),
    datetime.datetime(2024, 1, 10),
    datetime.datetime(2024, 2, 10),
    datetime.datetime(2024, 3, 10),
    datetime.datetime(2024, 4, 10),
    datetime.datetime(2024, 5, 10),
    datetime.datetime(2024, 6, 10),
    datetime.datetime(2024, 7, 10),
    datetime.datetime(2024, 8, 10),
    datetime.datetime(2024, 9, 10),
    datetime.datetime(2024, 10, 10),
    datetime.datetime(2024, 11, 10),
    datetime.datetime(2024, 12, 10),
    datetime.datetime(2025, 1, 10),
    datetime.datetime(2025, 2, 10),
    datetime.datetime(2025, 3, 10)
]

# Calculate XIRR
monthly_xirr = xirr(cash_flows, dates)
print(monthly_xirr)
# Calculate the effective interest rate based on XIRR
effective_rate = effective_interest_rate(monthly_xirr)
print(effective_rate)
# Output results
monthly_xirr_percentage = monthly_xirr * 100
effective_rate_percentage = effective_rate * 100
print(monthly_xirr_percentage)
print(effective_rate_percentage)
print(monthly_xirr_percentage, effective_rate_percentage)
