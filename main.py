  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_speed(distance, time):
        return distance / time