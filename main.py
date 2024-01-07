import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities