  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def calculate_roi(gain, cost):
        return (gain - cost) / cost