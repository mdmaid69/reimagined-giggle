  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])