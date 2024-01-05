import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)