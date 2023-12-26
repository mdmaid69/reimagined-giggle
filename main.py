def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)