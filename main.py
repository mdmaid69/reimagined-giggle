  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))