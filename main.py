def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen