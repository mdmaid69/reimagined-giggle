import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)