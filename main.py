  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps