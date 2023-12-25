import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)