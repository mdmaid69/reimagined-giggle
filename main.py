import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)