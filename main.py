def calculate_speed(distance, time):
        return distance / time
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime