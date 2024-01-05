import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities