import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def delete_file(file_name):
        os.remove(file_name)