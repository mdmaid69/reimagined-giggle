  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time