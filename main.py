  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h