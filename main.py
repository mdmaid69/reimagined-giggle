import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)