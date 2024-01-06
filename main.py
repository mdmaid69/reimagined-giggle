import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]