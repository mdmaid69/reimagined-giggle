import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time