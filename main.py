import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding