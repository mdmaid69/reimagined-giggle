  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal