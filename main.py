  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost