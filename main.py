import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]