  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities