def calculate_volume(length, width, height):
        return length * width * height
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns