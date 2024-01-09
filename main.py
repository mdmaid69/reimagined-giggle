import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue