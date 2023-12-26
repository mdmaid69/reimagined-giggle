import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])