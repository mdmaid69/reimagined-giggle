  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h