  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)