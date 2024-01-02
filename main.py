def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)