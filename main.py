import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]