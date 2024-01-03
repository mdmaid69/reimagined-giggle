  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time