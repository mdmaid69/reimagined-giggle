import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))