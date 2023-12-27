  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets