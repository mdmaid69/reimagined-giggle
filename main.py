def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)