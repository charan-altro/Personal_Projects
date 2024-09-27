from scipy.optimize import fsolve
from helper_functions import xirr, effective_interest_rate, generate_dates
import numpy as np

class CashFlowCalculator:
    def __init__(self, start_date, monthly_payment, total_months):
        self.start_date = start_date
        self.monthly_payment = monthly_payment
        self.total_months = total_months
        self.dates = generate_dates(self.start_date, months=self.total_months)
        self.cash_flows = []
        self.xirr_value = None
        self.effective_rate_value = None
        self.withdrawal_month = None
    
    def get_user_inputs(self):
        # Get user input: monthly payment, number of months, and XIRR or Effective Interest Rate
        choice = input("Would you like to input (1) XIRR or (2) Effective Interest Rate? Enter 1 or 2: ")
        self.withdrawal_month = int(input(f"Enter the month of withdrawal (1 to {self.total_months}): "))
        
        if choice == '1':
            self.xirr_value = float(input("Enter XIRR (as a percentage, e.g., 5 for 5%): ")) / 100
        elif choice == '2':
            self.effective_rate_value = float(input("Enter Effective Interest Rate (as a percentage, e.g., 6 for 6%): ")) / 100
        else:
            print("Invalid input. Please restart and select either 1 for XIRR or 2 for Effective Interest Rate.")
    
    def calculate_withdrawal_for_month(self):
        # Initial guess for withdrawal in the specified month
        withdrawal_guess = 85000
        
        def objective_function(w):
            # Generate cash flows for all months
            cash_flows = [-self.monthly_payment] * self.total_months
            cash_flows[self.withdrawal_month - 1] = w  # Set the withdrawal for the specified month
            
            if self.xirr_value is not None:
                # Calculate XIRR for all months
                calculated_xirr = xirr(cash_flows, self.dates)
                if calculated_xirr is None:
                    return float('inf')
                # Difference between calculated XIRR and user input
                return calculated_xirr - self.xirr_value
            
            elif self.effective_rate_value is not None:
                # Calculate average monthly rate for the first `self.total_months` months
                avg_monthly_rate = sum(cash_flows[:self.withdrawal_month]) / self.withdrawal_month

                # Ensure valid avg_monthly_rate for the effective interest rate calculation
                if avg_monthly_rate <= -1:
                    return float('inf')  # Invalid average rate
                
                calculated_effective_rate = effective_interest_rate(avg_monthly_rate)
                
                # Handle if effective interest rate calculation failed
                if calculated_effective_rate is None:
                    return float('inf')
                
                # Difference between calculated Effective Rate and user input
                return calculated_effective_rate - self.effective_rate_value
        
        # Use fsolve to calculate the withdrawal that matches XIRR or Effective Interest Rate
        withdrawal = fsolve(objective_function, withdrawal_guess)
        return withdrawal[0]

    def run(self):
        self.get_user_inputs()  # Step 1: Get user input for XIRR or Effective Interest Rate
        withdrawal = self.calculate_withdrawal_for_month()  # Step 2: Calculate the withdrawal amount
        print(f"Calculated Withdrawal for month {self.withdrawal_month}: {withdrawal}")

