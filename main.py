  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_perpetuity(payment, rate):
        return payment / rate