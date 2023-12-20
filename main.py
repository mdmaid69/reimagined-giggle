def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)