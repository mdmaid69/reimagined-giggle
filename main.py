import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)