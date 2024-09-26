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

# Start date for the first month
start_date = datetime.datetime(2023, 7, 10)

# Generate dynamic dates
dates = generate_dates(start_date, months=21)

# Cash flows with the given withdrawal amounts for each month (e.g., ₹85,000, ₹85,500, etc.)
withdrawals = [
    85000, 85500, 86000, 86500, 87000, 88000, 89000, 90000, 91000, 92000, 93000, 96000,
    98000, 101000, 104000, 106000, 109000, 112000, 115000, 116000, 117000
]
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



# Initialize lists to store results
xirr_results = []
effective_interest_results = []

# Iterate over each withdrawal and calculate Effective Interest Rate
for i, withdrawal in enumerate(withdrawals):
    # Calculate Average Monthly Rate and Effective Interest Rate for each month
    if i <= 12:    
        avg_monthly_rate = average_monthly_rate(withdrawal)
        effective_rate = effective_interest_rate(avg_monthly_rate)
    else:
        effective_rate = None
    # Generate cash flows: first month is the withdrawal, the rest are monthly investments (-5000)
    #member_cash_flows = [withdrawal] + [-5000] * 21
    # Store the results
    effective_interest_results.append(effective_rate * 100 if effective_rate is not None else "NA")  # Effective rate as percentage

# Iterate over each row of cash flows and calculate XIRR
for i, member_cash_flows in enumerate(cash_flows):
    # Try to calculate XIRR only for later months (starting with negative inflows)
    if i >= 12:  # You can adjust this index based on your pattern in Excel
        monthly_xirr = xirr(member_cash_flows, dates)
    else:
        monthly_xirr = None
        # Store the results
    xirr_results.append(monthly_xirr * 100 if monthly_xirr is not None else "NA")  # XIRR as percentage

# Output the results for each member
for i in range(len(withdrawals)):
    print(f"Member {i+1}: XIRR = {xirr_results[i]}, Effective Interest Rate = {effective_interest_results[i]}")
