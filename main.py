  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets