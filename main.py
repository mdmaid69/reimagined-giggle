  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time