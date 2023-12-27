def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)