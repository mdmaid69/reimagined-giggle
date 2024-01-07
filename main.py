  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))