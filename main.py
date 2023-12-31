  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time