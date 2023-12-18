def greet(name):
        print(f"Hello, {name}!")
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)