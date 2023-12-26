import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))