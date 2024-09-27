from scipy.optimize import fsolve
from helper_functions import xirr, effective_interest_rate, generate_dates
import numpy as np

class CashFlowCalculator:
    def __init__(self, start_date, monthly_payment):
        self.start_date = start_date
        self.monthly_payment = monthly_payment
        self.dates = generate_dates(self.start_date)
        self.cash_flows = []
        self.xirr_values = []
        self.effective_rate_values = []
    
    def get_user_inputs(self):
        # Get XIRR values for the last 8 months (14th to 21st month)
        xirr_input = input("Enter XIRR values for the last 8 months (comma-separated): ")
        self.xirr_values = [float(x) / 100 for x in xirr_input.split(",")]  # Convert percentages to decimal

        # Get Effective Interest Rate values for the first 13 months (1st to 13th month)
        eff_rate_input = input("Enter Effective Interest Rate values for the first 13 months (comma-separated): ")
        self.effective_rate_values = [float(x) / 100 for x in eff_rate_input.split(",")]  # Convert percentages to decimal
    
    def calculate_withdrawals(self):
        # Initial guesses for the withdrawals
        withdrawals = np.linspace(85000, 117000, num=21)
        
        def objective_function(w):
            # Generate cash flows based on proposed withdrawal amounts
            cash_flows = [[w[i]] + [-self.monthly_payment] * (21 - 1) for i in range(21)]
            
            # Calculate XIRR for the last 8 months (months 14 to 21)
            xirr_diffs = []
            for i in range(8):
                cash_flows_last_month = [cf[13 + i] for cf in cash_flows]  # cash flow for the ith month in the last 8 months
                xirr_calculated = xirr(cash_flows_last_month, self.dates[13 + i:])
                if xirr_calculated is None:
                    xirr_diffs.append(float('inf'))
                else:
                    xirr_diffs.append(xirr_calculated - self.xirr_values[i])  # Difference from user input

            # Calculate Effective Interest Rate for the first 13 months
            eff_rate_diffs = []
            for i in range(13):
                cash_flows_first_month = [cf[i] for cf in cash_flows]  # cash flow for the ith month in the first 13 months
                avg_monthly_rate = np.mean(cash_flows_first_month)  # simple average for the month
                eff_rate_calculated = effective_interest_rate(avg_monthly_rate)
                eff_rate_diffs.append(eff_rate_calculated - self.effective_rate_values[i])  # Difference from user input

            # Combine XIRR and Effective Rate differences for the objective function
            return xirr_diffs + eff_rate_diffs

        # Use fsolve to adjust withdrawals to match the input XIRR and Effective Interest Rate
        withdrawals = fsolve(objective_function, withdrawals)
        return withdrawals

    def run(self):
        self.get_user_inputs()  # Get user input for XIRR and Effective Interest Rate
        withdrawals = self.calculate_withdrawals()  # Calculate withdrawals based on the inputs
        print(f"Calculated Withdrawals: {withdrawals}")
