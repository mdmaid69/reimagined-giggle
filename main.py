numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)