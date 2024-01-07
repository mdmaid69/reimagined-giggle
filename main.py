def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)