import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)