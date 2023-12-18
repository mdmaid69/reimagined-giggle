  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps