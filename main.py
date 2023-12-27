  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets