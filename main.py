import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)