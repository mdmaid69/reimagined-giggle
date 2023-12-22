def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)