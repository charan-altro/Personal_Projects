import numpy as np
from scipy.optimize import newton, fsolve
import datetime
from calc_functions import xirr, effective_interest_rate, average_monthly_rate, generate_dates

class CashFlowCalculator:
    def __init__(self, start_date):
        self.start_date = start_date
        self.dates = generate_dates(self.start_date)
        self.cash_flows = []
    
    def get_user_inputs(self):
        # Get XIRR and Effective Interest Rate from the user
        self.input_xirr = float(input("Enter XIRR for the last 8 months (as a percentage, e.g., 5 for 5%): ")) / 100
        self.input_effective_rate = float(input("Enter Effective Interest Rate for the first 13 months (as a percentage, e.g., 6 for 6%): ")) / 100
    
    def calculate_withdrawals(self):
        # Use optimization to find the withdrawals that match the input XIRR and Effective Interest Rate
        withdrawals = [85000 + i * 500 for i in range(21)]  # Initial guesses for withdrawals, similar to previous logic
        
        def objective_function(w):
            # Generate cash flows based on proposed withdrawal amounts
            cash_flows = [[w[i]] + [-5000] * (21 - 1) for i in range(21)]
            
            # Calculate XIRR for the last 8 months (months 14 to 21)
            cash_flows_last_8 = [cf[-8:] for cf in cash_flows]
            dates_last_8 = self.dates[-8:]
            xirr_last_8 = xirr([cf[0] for cf in cash_flows_last_8], dates_last_8)
            
            # Calculate Effective Interest Rate for the first 13 months
            avg_monthly_rate = (1 + self.input_effective_rate) ** (21 / 12) - 1
            effective_rate_first_13 = effective_interest_rate(avg_monthly_rate)
            
            # Objective: Minimize the difference between calculated XIRR and input XIRR,
            # and calculated Effective Interest Rate and input Effective Interest Rate
            return [
                xirr_last_8 - self.input_xirr,
                effective_rate_first_13 - self.input_effective_rate
            ]
        
        # Use fsolve to solve for the withdrawal amounts that meet the objective function
        withdrawals = fsolve(objective_function, withdrawals)
        return withdrawals

    def run(self):
        self.get_user_inputs()  # Step 1: Get user input for XIRR and Effective Interest Rate
        withdrawals = self.calculate_withdrawals()  # Step 2: Calculate withdrawals based on the inputs
        print(f"Calculated Withdrawals: {withdrawals}")

# Start date
start_date = datetime.datetime(2023, 7, 10)

# Initialize the calculator and run
calculator = CashFlowCalculator(start_date)
calculator.run()
