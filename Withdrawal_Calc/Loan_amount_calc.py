import numpy as np

class LoanWithdrawalCalculator:
    def __init__(self, monthly_payment, total_months):
        self.monthly_payment = monthly_payment
        self.total_months = total_months
        self.withdrawal_month = None
        self.effective_rate_value = None

    def get_user_inputs(self):
        # Get the month of withdrawal and effective interest rate from the user
        self.withdrawal_month = int(input(f"Enter the month of withdrawal (1 to {self.total_months}): "))
        self.effective_rate_value = float(input("Enter Effective Interest Rate (as a percentage, e.g., 6 for 6%): ")) / 100

    def calculate_withdrawal_for_month(self):
        # Convert the effective annual interest rate to a monthly interest rate
        monthly_rate = (1 + self.effective_rate_value) ** (1 / 12) - 1

        # Calculate the present value of the loan (withdrawal amount)
        if monthly_rate != 0:
            # Present value using the formula for a loan (present value of an annuity)
            present_value = self.monthly_payment * (1 - (1 + monthly_rate) ** -self.total_months) / monthly_rate
        else:
            # In case of a zero interest rate, the present value is just the total payments
            present_value = self.monthly_payment * self.total_months

        return present_value

    def run(self):
        self.get_user_inputs()  # Step 1: Get user input for Effective Interest Rate and withdrawal month
        withdrawal = self.calculate_withdrawal_for_month()  # Step 2: Calculate the withdrawal amount
        print(f"Calculated Withdrawal for month {self.withdrawal_month}: {withdrawal:.2f}")




#from Loan_amount_calc import LoanWithdrawalCalculator

# Get inputs
monthly_payment = float(input("Enter your monthly payment (e.g., 5000, 10000, 20000): "))
total_months = int(input("Enter the total number of months: "))

# Initialize the calculator and run
calculator = LoanWithdrawalCalculator(monthly_payment, total_months)
calculator.run()
