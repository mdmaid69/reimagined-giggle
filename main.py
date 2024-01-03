  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets