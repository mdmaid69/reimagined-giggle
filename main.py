import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])