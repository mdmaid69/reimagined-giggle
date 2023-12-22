import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]