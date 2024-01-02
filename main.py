  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets