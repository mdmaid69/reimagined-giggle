  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets