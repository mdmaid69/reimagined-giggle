text = "Hello, world!"
print("Characters:", len(text))
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)