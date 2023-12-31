  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)