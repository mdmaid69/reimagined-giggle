import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)