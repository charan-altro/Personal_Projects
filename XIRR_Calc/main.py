from cashflow_calculator import CashFlowCalculator
import datetime

# Set the start date and file paths
start_date = datetime.datetime(2023, 7, 10)
withdrawal_file = 'withdrawals.txt'  # Path to your withdrawals file
cashflow_file = 'cashflow_data.csv'       # Path to your cash flow CSV file

# Create an instance of the CashFlowCalculator
calculator = CashFlowCalculator(start_date, withdrawal_file, cashflow_file)

# Run the calculations
calculator.run_calculations()
