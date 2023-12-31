import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)