import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])