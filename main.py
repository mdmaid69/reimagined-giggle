def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)