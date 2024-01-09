text = "Hello, world!"
print("Uppercase:", text.upper())
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)