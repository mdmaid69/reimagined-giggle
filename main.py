  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets