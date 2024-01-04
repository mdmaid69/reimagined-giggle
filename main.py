  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))