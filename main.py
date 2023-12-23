  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time