import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_average(lst):
        return sum(lst) / len(lst)