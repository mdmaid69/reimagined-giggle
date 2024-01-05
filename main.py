  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps