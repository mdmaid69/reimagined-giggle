import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))