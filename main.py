  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import itertools
print(list(itertools.permutations([1, 2, 3])))