def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink