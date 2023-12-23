  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding