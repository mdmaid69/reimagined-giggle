def calculate_perpetuity(payment, rate):
        return payment / rate
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)