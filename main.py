  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import itertools
print(list(itertools.permutations([1, 2, 3])))