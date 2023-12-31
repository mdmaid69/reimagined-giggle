  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def calculate_acceleration(speed, time):
        return speed / time