  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import itertools
print(list(itertools.permutations([1, 2, 3])))