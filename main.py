  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])