  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)