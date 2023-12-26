n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)