import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)