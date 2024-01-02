  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
for i in range(5):
        print(i)