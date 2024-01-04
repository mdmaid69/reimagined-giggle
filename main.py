  import os
  def get_current_directory():
        return os.getcwd()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)