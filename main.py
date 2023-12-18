import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def get_base_name(path):
        return os.path.basename(path)