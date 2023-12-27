  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities