  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)