  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))