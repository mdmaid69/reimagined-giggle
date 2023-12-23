  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)