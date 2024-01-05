  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import itertools
print(list(itertools.permutations([1, 2, 3])))