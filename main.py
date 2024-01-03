  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost