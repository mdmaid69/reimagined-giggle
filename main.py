  import os
  def get_base_name(path):
        return os.path.basename(path)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)