  import os
  def delete_file(file_name):
        os.remove(file_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])