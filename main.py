  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time