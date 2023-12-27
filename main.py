import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
text = "Hello, world!"
print("Reversed:", text[::-1])