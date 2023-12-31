import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)