  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)