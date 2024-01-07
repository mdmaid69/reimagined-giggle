import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)