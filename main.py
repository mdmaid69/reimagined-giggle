import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)