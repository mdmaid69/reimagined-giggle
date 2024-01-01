  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)