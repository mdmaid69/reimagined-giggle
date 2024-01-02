import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)