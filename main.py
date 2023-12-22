import itertools
print(list(itertools.permutations([1, 2, 3])))
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]