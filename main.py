def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)