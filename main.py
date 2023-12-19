def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)