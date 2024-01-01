  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import itertools
print(list(itertools.permutations([1, 2, 3])))