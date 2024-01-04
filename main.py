  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])