  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity