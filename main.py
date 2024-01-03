  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def calculate_circumference_circle(r):
        return 2 * 3.14 * r