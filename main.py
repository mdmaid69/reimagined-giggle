  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)