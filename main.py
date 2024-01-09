  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))