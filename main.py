numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)