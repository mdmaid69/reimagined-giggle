  import os
  def delete_file(file_name):
        os.remove(file_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)