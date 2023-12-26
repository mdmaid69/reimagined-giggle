import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))