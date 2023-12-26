  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))