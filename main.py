  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time