  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def calculate_volume(length, width, height):
        return length * width * height