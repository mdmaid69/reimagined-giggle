  import os
  def split_path(path):
        return os.path.split(path)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)