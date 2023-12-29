import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)