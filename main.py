def calculate_volume(length, width, height):
        return length * width * height
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen