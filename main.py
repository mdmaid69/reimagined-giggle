  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def calculate_speed(distance, time):
        return distance / time