def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)