  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))