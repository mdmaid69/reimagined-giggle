  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities