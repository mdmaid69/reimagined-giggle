  import os
  def split_path(path):
        return os.path.split(path)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time