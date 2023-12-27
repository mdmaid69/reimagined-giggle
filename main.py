  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import itertools
print(list(itertools.permutations([1, 2, 3])))