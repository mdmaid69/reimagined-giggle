  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)