  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time