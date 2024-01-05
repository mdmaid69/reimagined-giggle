import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)