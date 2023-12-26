import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)