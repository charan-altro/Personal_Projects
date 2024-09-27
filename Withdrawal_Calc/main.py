from cashflow_calculator import CashFlowCalculator
import datetime

# Set the start date and get the user input for monthly payment
start_date = datetime.datetime(2023, 7, 10)
monthly_payment = float(input("Enter your monthly payment (e.g., 5000, 10000, 20000): "))
total_months = int(input("Enter the total number of months: "))

# Initialize the calculator and run
calculator = CashFlowCalculator(start_date, monthly_payment, total_months)
calculator.run()
