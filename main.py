  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity