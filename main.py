  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding