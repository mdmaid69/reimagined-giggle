import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))