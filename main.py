  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import itertools
print(list(itertools.permutations([1, 2, 3])))