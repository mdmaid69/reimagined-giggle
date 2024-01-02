  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev