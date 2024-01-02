  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)