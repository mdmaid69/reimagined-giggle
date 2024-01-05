  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import itertools
print(list(itertools.permutations([1, 2, 3])))