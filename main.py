import itertools
print(list(itertools.permutations([1, 2, 3])))
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)