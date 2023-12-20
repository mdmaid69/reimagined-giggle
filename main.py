  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import itertools
print(list(itertools.permutations([1, 2, 3])))