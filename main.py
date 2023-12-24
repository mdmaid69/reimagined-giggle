import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])