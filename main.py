  import os
  def delete_file(file_name):
        os.remove(file_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))