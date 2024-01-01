  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps