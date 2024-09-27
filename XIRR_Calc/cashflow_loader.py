import csv

# Load cash flows from a CSV file (where each row is a list of cash flows for each member)
def load_cash_flows_from_csv(file_path):
    cash_flows = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Convert each row of cash flows to a list of floats (handle any necessary cleaning here)
            cash_flows.append([float(item) for item in row])
    return cash_flows

# Load withdrawals from a separate text or CSV file
def load_withdrawals(file_path):
    withdrawals = []
    with open(file_path, 'r') as file:
        for line in file:
            withdrawals.append(float(line.strip()))  # Convert withdrawal amounts to float
    return withdrawals
