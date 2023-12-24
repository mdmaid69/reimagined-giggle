  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)