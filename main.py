  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)