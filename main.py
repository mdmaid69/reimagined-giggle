import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def delete_file(file_name):
        os.remove(file_name)