  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import itertools
print(list(itertools.permutations([1, 2, 3])))