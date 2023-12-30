  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)