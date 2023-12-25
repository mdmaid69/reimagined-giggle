import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)