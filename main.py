import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)