def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns