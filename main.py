import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)