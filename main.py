  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import itertools
print(list(itertools.permutations([1, 2, 3])))