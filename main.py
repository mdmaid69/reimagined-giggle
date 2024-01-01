  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets