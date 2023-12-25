  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import itertools
print(list(itertools.permutations([1, 2, 3])))