  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import itertools
print(list(itertools.permutations([1, 2, 3])))