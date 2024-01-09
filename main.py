import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)