  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))