  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import itertools
print(list(itertools.permutations([1, 2, 3])))