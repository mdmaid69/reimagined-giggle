import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize