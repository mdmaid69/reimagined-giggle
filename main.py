import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))