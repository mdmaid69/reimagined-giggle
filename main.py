  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def calculate_area_rectangle(l, w):
        return l * w