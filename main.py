import shutil
def delete_directory(path):
        shutil.rmtree(path)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"