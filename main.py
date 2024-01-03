def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)