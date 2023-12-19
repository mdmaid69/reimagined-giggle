  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import itertools
print(list(itertools.permutations([1, 2, 3])))