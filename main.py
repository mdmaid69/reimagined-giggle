n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)