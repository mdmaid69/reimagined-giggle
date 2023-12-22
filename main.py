def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)