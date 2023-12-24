  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def calculate_area_rectangle(l, w):
        return l * w