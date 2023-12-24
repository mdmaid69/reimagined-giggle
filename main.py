import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino