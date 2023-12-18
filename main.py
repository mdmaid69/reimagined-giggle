  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time