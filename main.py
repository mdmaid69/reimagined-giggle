  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()