  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding