  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps