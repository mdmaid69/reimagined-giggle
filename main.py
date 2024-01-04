n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)