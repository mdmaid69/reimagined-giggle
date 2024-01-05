  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())