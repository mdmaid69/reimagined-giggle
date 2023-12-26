  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps