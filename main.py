  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps