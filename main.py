  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding