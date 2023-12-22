  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps