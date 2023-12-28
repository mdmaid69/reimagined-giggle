def calculate_volume(length, width, height):
        return length * width * height
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize