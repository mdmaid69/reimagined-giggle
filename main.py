import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)