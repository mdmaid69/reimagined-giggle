  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)