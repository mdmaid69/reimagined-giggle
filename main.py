def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)