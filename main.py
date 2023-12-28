import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)