def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)