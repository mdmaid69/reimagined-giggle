def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)