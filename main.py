  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding