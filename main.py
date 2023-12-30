import itertools
print(list(itertools.permutations([1, 2, 3])))
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)