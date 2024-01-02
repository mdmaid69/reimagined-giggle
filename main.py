import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets