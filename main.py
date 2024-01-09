  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])