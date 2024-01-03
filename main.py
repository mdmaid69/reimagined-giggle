import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)