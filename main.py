  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time