def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)