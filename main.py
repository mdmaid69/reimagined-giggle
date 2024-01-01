text = "Hello, world!"
print("Uppercase:", text.upper())
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)