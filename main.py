import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
text = "Hello, world!"
print("Reversed:", text[::-1])