  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def calculate_volume(length, width, height):
        return length * width * height