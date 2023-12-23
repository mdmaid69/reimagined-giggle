  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))