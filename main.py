  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)