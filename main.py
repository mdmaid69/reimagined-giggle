  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time