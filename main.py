def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)