import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))