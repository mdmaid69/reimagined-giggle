  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import shutil
def delete_directory(path):
        shutil.rmtree(path)