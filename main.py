  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time