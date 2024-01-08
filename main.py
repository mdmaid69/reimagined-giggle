import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)