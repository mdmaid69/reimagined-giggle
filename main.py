  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
i = 0
while i < 5:
        print(i)
        i += 1