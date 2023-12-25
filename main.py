  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import itertools
print(list(itertools.permutations([1, 2, 3])))