  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding