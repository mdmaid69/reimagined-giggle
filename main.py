  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))