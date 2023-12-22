  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps