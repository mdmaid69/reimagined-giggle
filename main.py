import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)