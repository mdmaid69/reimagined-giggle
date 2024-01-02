  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps