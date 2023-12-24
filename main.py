import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])