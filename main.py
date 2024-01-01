  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding