  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time