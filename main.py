  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import itertools
print(list(itertools.permutations([1, 2, 3])))