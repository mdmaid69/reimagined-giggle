import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)