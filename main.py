  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding