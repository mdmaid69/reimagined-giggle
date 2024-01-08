def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)