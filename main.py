  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import itertools
print(list(itertools.permutations([1, 2, 3])))