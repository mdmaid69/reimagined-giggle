def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size