def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)