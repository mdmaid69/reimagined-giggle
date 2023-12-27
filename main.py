  import os
  def get_base_name(path):
        return os.path.basename(path)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)