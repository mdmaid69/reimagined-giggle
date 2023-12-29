def reverse_list(lst):
        return lst[::-1]
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)