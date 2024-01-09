import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)