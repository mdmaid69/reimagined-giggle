import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def split_path(path):
        return os.path.split(path)