import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)