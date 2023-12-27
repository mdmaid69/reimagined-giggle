  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity