  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps