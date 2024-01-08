  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets