  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)