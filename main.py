import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
x = 10
y = 20
print("Sum:", x + y)