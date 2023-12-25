  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding