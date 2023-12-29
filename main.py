import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)