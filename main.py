  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def calculate_volume(length, width, height):
        return length * width * height