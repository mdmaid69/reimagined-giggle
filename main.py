  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
for i in range(5):
        print(i)