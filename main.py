import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)