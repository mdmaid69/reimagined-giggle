numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)