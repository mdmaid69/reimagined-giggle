def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns