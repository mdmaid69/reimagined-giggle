  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding