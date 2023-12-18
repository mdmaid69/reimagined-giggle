  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a