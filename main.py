text = "Hello, world!"
print("Reversed:", text[::-1])
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)