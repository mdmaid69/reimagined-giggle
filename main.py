  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time