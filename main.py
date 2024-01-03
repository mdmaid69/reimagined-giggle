  import os
  def get_current_working_directory():
        return os.getcwd()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)