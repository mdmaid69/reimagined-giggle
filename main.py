  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time