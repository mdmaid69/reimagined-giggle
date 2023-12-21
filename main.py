  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)