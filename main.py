  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import itertools
print(list(itertools.permutations([1, 2, 3])))