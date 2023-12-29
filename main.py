def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)