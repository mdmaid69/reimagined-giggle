  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])