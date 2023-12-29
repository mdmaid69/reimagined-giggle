  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal