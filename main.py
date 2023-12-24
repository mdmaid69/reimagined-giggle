  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)