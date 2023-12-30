  import os
  def split_path(path):
        return os.path.split(path)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time