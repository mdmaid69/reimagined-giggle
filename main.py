  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import itertools
print(list(itertools.permutations([1, 2, 3])))