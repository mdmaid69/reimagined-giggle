  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import shutil
def delete_directory(path):
        shutil.rmtree(path)