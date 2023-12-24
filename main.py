import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)