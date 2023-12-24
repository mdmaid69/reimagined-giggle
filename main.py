  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets