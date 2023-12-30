  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time