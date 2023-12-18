  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def delete_file(file_name):
        os.remove(file_name)