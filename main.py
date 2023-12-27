def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)