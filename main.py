import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)