  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import itertools
print(list(itertools.permutations([1, 2, 3])))