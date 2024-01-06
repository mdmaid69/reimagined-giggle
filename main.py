  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets