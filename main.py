def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)