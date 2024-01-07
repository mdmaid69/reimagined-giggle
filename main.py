def greet(name):
        print(f"Hello, {name}!")
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)