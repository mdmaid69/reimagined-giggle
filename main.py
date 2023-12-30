def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def delete_file(file_name):
        os.remove(file_name)