import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])