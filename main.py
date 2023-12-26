  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps