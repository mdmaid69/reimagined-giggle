  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time