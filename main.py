  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)