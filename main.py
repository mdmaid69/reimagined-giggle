  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time