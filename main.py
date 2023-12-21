def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]