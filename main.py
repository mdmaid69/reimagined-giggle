import itertools
print(list(itertools.permutations([1, 2, 3])))
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)