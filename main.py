  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)