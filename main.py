  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps