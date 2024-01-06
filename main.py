n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)