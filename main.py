  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)