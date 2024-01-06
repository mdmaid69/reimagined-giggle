  import os
  def split_path(path):
        return os.path.split(path)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)