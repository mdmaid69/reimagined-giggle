import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)