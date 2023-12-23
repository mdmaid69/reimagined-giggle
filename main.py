  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets