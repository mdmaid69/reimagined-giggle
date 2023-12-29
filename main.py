def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)