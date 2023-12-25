  import os
  def get_base_name(path):
        return os.path.basename(path)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])