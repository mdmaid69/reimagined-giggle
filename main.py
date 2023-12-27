def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)