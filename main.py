  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets