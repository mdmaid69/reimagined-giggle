import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)