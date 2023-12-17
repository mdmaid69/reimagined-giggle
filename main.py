  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def calculate_volume(length, width, height):
        return length * width * height