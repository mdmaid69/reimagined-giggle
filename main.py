  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def calculate_volume(length, width, height):
        return length * width * height