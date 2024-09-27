from calc_functions import xirr, average_monthly_rate, effective_interest_rate, generate_dates
from cashflow_loader import load_cash_flows_from_csv, load_withdrawals
import datetime

class CashFlowCalculator:
    def __init__(self, start_date, withdrawal_file, cashflow_file):
        self.start_date = start_date
        self.dates = generate_dates(self.start_date)
        self.withdrawals = load_withdrawals(withdrawal_file)  # Load withdrawals
        self.cash_flows = load_cash_flows_from_csv(cashflow_file)  # Load cash flows from file
        self.xirr_results = []
        self.effective_interest_results = []

    def calculate_effective_interest_rates(self):
        for i, withdrawal in enumerate(self.withdrawals):
            if i <= 12:    
                avg_monthly_rate = average_monthly_rate(withdrawal)
                effective_rate = effective_interest_rate(avg_monthly_rate)
            else:
                effective_rate = None
            # Store the effective rate results
            self.effective_interest_results.append(effective_rate * 100 if effective_rate is not None else "NA")

    def calculate_xirr(self):
        for i, member_cash_flows in enumerate(self.cash_flows):
            if i >= 12:  # XIRR calculation only for later months
                monthly_xirr = xirr(member_cash_flows, self.dates)
            else:
                monthly_xirr = None
            # Store the XIRR results
            self.xirr_results.append(monthly_xirr * 100 if monthly_xirr is not None else "NA")

    def display_results(self):
        for i in range(len(self.withdrawals)):
            print(f"Member {i+1}: XIRR = {self.xirr_results[i]}, Effective Interest Rate = {self.effective_interest_results[i]}")

    def run_calculations(self):
        self.calculate_effective_interest_rates()
        self.calculate_xirr()
        self.display_results()
