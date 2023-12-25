  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets