  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_acceleration(speed, time):
        return speed / time