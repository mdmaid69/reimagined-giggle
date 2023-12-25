import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)