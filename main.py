  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time