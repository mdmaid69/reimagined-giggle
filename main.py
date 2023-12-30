import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))