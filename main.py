import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def delete_file(file_name):
        os.remove(file_name)