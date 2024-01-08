  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps