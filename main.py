import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))