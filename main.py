  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time