import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)