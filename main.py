  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]