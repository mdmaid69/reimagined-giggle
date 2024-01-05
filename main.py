def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)