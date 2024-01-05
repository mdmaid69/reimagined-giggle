import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)