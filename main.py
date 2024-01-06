  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import itertools
print(list(itertools.permutations([1, 2, 3])))