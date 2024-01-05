  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)