  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets