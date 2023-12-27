def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)