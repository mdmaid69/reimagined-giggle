n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)