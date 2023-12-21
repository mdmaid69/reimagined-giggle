def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)