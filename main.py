  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def calculate_roi(gain, cost):
        return (gain - cost) / cost