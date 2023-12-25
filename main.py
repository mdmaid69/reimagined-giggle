  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))