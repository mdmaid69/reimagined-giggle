  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import itertools
print(list(itertools.permutations([1, 2, 3])))