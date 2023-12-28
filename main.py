  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))