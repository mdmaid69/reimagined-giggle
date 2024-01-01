  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_volume(length, width, height):
        return length * width * height