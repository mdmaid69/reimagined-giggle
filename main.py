  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps