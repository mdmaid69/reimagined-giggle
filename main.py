def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns