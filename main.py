  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)