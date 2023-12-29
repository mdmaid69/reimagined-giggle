  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)