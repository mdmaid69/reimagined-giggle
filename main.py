  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def delete_file(file_name):
        os.remove(file_name)