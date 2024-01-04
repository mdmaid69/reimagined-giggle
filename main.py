  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_perpetuity(payment, rate):
        return payment / rate