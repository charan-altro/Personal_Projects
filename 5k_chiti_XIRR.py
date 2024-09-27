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
def average_monthly_rate(cash_flow):
    return (100000 - cash_flow) / 105000

# Helper function to calculate the Effective Interest Rate based on Average Monthly Rate
def effective_interest_rate(avg_monthly_rate):
    if avg_monthly_rate is None:
        return None
    return (1 + avg_monthly_rate) ** (12 / 21) - 1

first_month_cash_flows = [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000]


# Predefined Average Monthly Rate (for early months where XIRR isn't calculated)
#average_monthly_rates = [0.14, 0.14, 0.13, 0.13, 0.12, 0.11, 0.10, 0.10, 0.09, 0.08, 0.07, 0.04, 0.02, None, None, None, None, None, None, None, None]
# Cash flow data (21 rows, 21 months per row, borrowing and repayment)
cash_flows = [
    [85000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, 85500, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, 86000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, 86500, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, 87000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, 88000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, 89000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, 90000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 91000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 92000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 93000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 96000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 98000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 101000, -5000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 104000, -5000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 106000, -5000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 109000, -5000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 112000, -5000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 115000, -5000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 116000, -5000],
    [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, 117000],
]

# Corresponding dates for the 21 months
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

# Initialize lists to store results
xirr_results = []
effective_interest_results = []

# Iterate over each row of cash flows
for i, member_cash_flows in enumerate(cash_flows):
    # Try to calculate XIRR only for later months (starting with negative inflows)
    if i >= 12:  # You can adjust this index based on your pattern in Excel
        monthly_xirr = xirr(member_cash_flows, dates)
    else:
        monthly_xirr = None
    
    if monthly_xirr is None:
        # Calculate Average Monthly Rate based on cash flow for the first repayment month (similar to C2 in Excel)
        avg_monthly_rate = average_monthly_rate(member_cash_flows[0])  # Assume first cash flow corresponds to C2
        effective_rate = effective_interest_rate(avg_monthly_rate)
    else:
        # Calculate effective interest rate if XIRR calculation succeeded
        effective_rate = effective_interest_rate(monthly_xirr)
    
    # Store the results
    xirr_results.append(monthly_xirr * 100 if monthly_xirr is not None else "NA")  # XIRR as percentage
    effective_interest_results.append(effective_rate * 100 if effective_rate is not None else "NA")  # Effective rate as percentage

# Output the results for each member
for i in range(len(cash_flows)):
    print(f"Member {i+1}: XIRR = {xirr_results[i]}, Effective Interest Rate = {effective_interest_results[i]}")
