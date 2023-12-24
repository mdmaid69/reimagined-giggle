def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)